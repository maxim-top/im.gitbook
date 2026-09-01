#!/usr/bin/env python3
import argparse
import re
from pathlib import Path, PurePosixPath


LINK_PATTERN = re.compile(r'\[(.*)\]\((.*)\)')
LINK_TITLES = {
    '.': '以下是本节中的文章：',
    'zh-hans': '以下是本节中的文章：',
    'en': 'Here are the articles in this section:',
}


def header_size(line):
    prefix = line[:len(line) - len(line.lstrip(' *'))]
    return len(prefix) if '*' in prefix else 0


def parse_line(line):
    match = LINK_PATTERN.search(line)
    if not match:
        raise ValueError(f'Invalid SUMMARY entry: {line}')
    return match.group(1), match.group(2)


def markdown_to_url(path):
    return path.replace('.md', '.html', 1)


def markdown_to_html(path):
    return path.replace('README.md', 'index.html', 1).replace('.md', '.html', 1)


def relative_link(parent_link, link):
    parent_parts = [part for part in (markdown_to_url(parent_link) + '/').split('/') if part]
    link_url = markdown_to_url(link)
    link_parts = [part for part in (link_url + '/').split('/') if part]
    common = 0
    while common < min(len(parent_parts), len(link_parts)):
        if parent_parts[common] != link_parts[common]:
            break
        common += 1
    result = '/'.join(
        ['..'] * max(0, len(parent_parts[common:]) - 1) + link_parts[common:])
    if link_url.endswith('/'):
        result += '/'
    return result.replace('README.html', '', 1)


def direct_children(lines, start, parent_size):
    children = []
    for line in lines[start:]:
        size = header_size(line)
        if size <= parent_size:
            break
        if size == parent_size + 2:
            children.append(line)
    return children


def render_children(children, language, parent_link, list_template, link_template):
    rendered_links = []
    for child in children:
        title, link = parse_line(child)
        rendered_link = link_template.replace('{{text}}', title, 1)
        rendered_link = rendered_link.replace(
            '{{url}}', relative_link(parent_link, link), 1)
        rendered_links.append(rendered_link)
    rendered = list_template.replace('{{links}}', ''.join(rendered_links), 1)
    return rendered.replace('{{links_title}}', LINK_TITLES[language], 1)


def process_summary(site_dir, summary_file, list_template, link_template):
    lines = [line for line in summary_file.read_text().splitlines() if line]
    relative_parent = summary_file.parent.relative_to(site_dir)
    language = '.' if str(relative_parent) == '.' else relative_parent.parts[0]

    for index, parent in enumerate(lines):
        parent_size = header_size(parent)
        if not parent_size:
            continue
        children = direct_children(lines, index + 1, parent_size)
        if not children:
            continue
        _, parent_link = parse_line(parent)
        markdown_file = summary_file.parent / PurePosixPath(parent_link)
        markdown_lines = [line for line in markdown_file.read_text().splitlines() if line]
        if len(markdown_lines) > 2:
            continue
        html_path = markdown_to_html((relative_parent / PurePosixPath(parent_link)).as_posix())
        html_file = site_dir / '_book' / html_path
        html = html_file.read_bytes()
        if b'link_item' in html:
            continue
        summary_html = render_children(
            children, language, parent_link, list_template, link_template).encode()
        html_file.write_bytes(html.replace(b'<footer ', summary_html + b'<footer ', 1))


def add_subdirectory_summaries(site_dir):
    site_dir = Path(site_dir)
    list_template = (site_dir / 'scripts/subdirectory_summary.html').read_text()
    link_template = (site_dir / 'scripts/subdirectory_summary_link.html').read_text()
    summary_files = []
    root_summary = site_dir / 'SUMMARY.md'
    if root_summary.is_file():
        summary_files.append(root_summary)
    summary_files.extend(sorted(site_dir.glob('*/SUMMARY.md')))
    for summary_file in summary_files:
        process_summary(site_dir, summary_file, list_template, link_template)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--site-dir', required=True)
    args = parser.parse_args()
    add_subdirectory_summaries(args.site_dir)


if __name__ == '__main__':
    main()
