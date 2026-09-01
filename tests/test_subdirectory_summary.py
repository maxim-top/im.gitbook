import os
import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
import subdirectory_summary


class SubdirectorySummaryTest(unittest.TestCase):
    def create_site(self, directory, language=None):
        site = Path(directory)
        source = site if language is None else site / language
        output = site / '_book' if language is None else site / '_book' / language
        (site / 'scripts').mkdir()
        (source / 'section').mkdir(parents=True)
        (output / 'section').mkdir(parents=True)
        (site / 'scripts/subdirectory_summary.html').write_text(
            '<nav>{{links_title}}{{links}}</nav>')
        (site / 'scripts/subdirectory_summary_link.html').write_text(
            '<a class="link_item" href="{{url}}">{{text}}</a>')
        (source / 'SUMMARY.md').write_text(
            '* [Section](section/README.md)\n  * [Article](section/article.md)\n')
        (source / 'section/README.md').write_text('# Section\n')
        (source / 'section/article.md').write_text('# Article\n')
        (output / 'section/index.html').write_bytes(b'<main></main><footer test>')
        return site, output / 'section/index.html'

    def test_processes_single_language_root_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            site, html_file = self.create_site(directory)

            subdirectory_summary.add_subdirectory_summaries(site)

            self.assertEqual(
                '<main></main><nav>以下是本节中的文章：'
                '<a class="link_item" href="article.html">Article</a></nav><footer test>',
                html_file.read_text(),
            )

    def test_processes_multilingual_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            site, html_file = self.create_site(directory, 'en')

            subdirectory_summary.add_subdirectory_summaries(site)

            self.assertIn(
                '<nav>Here are the articles in this section:',
                html_file.read_text(),
            )

    def test_does_not_duplicate_existing_summary(self):
        with tempfile.TemporaryDirectory() as directory:
            site, html_file = self.create_site(directory)

            subdirectory_summary.add_subdirectory_summaries(site)
            first = html_file.read_bytes()
            subdirectory_summary.add_subdirectory_summaries(site)

            self.assertEqual(first, html_file.read_bytes())


if __name__ == '__main__':
    unittest.main()
