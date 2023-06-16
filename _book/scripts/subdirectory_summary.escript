#!/usr/bin/env escript
%% -*- mode: erlang;erlang-indent-level: 4;indent-tabs-mode: nil -*-
%% ex: ft=erlang ts=4 sw=4 et
main(_Args) ->
    {ok, LinkListHtml} = file:read_file("scripts/subdirectory_summary.html"),
    {ok, LinkHtml} = file:read_file("scripts/subdirectory_summary_link.html"),
    put(linklist_html, LinkListHtml),
    put(link_html, LinkHtml),
    SummaryFiles = filelib:wildcard("*/SUMMARY.md"),
    lists:foreach(fun (E) -> process_summary(E) end, SummaryFiles),
    ok.

process_summary(SummaryFile) ->
    {ok, Bin} = file:read_file(SummaryFile),
    Lines = string:tokens(binary_to_list(Bin), "\r\n"),
    process_summary_1(SummaryFile, Lines),
    ok.

process_summary_1(SummaryFile, [Line|Lines]) ->
    case header_size(Line) of
        0 ->
            process_summary_1(SummaryFile, Lines);
        HeaderSize ->
            Children = get_children(Lines, HeaderSize, []),
            maybe_gen_summary(Line, Children,SummaryFile),
            process_summary_1(SummaryFile, Lines)
    end;
process_summary_1(_SummaryFile, []) ->
    ok.

maybe_gen_summary(_Parent, [], _SummaryFile) ->
    ok;
maybe_gen_summary(Parent, Children, SummaryFile) ->
    {_Title, Link} = parse_line(Parent),
    BaseDir = filename:dirname(SummaryFile),
    LinkFile = filename:join(BaseDir, Link),
    {ok, LinkData} = file:read_file(LinkFile),
    LinkLines = length(string:tokens(binary_to_list(LinkData),"\r\n")),
    case LinkLines =< 2 of
        true ->
            %%io:format("Title:~ts, Link:~ts, LinkLines:~p~n", [Title, Link, LinkLines]),
            gen_summary(LinkFile, Children, BaseDir, Link);
        false ->
            skip
    end,
    ok.

gen_summary(LinkFile, Children, BaseDir, ParentLink) ->
    LinkHtmlFile = markdown_to_html_file(LinkFile),
    %%io:format("file:~ts~n", [LinkHtmlFile]),
    {ok, Bin} = file:read_file(LinkHtmlFile),
    case re:run(Bin, "link_item", [global]) of
        {match, _} ->
            skip;
        nomatch ->
            SummaryHtml = gen_summary_html(Children, BaseDir, ParentLink),
            %%io:format("SummaryHtml:~ts~n", [SummaryHtml]),
            PositionHtml = <<"<footer ">>,
            NewBin = binary:replace(Bin, PositionHtml, <<SummaryHtml/binary, PositionHtml/binary>>),
            ok = file:write_file(LinkHtmlFile, NewBin)
    end.

gen_summary_html(Children, BaseDir, ParentLink) ->
    AllLinkHtml = lists:map(
        fun (Line) ->
            {Title, Link} = parse_line(Line),
            NewLink = make_relative_link(ParentLink, Link),
            %%io:format("Relative: Title=~ts, ParentLink=~ts, Link=~ts, NewLink=~ts~n", [Title, ParentLink, Link, NewLink]),
            LinkHtml = get(link_html),
            LinkHtml1 = binary:replace(LinkHtml, <<"{{text}}">>, list_to_binary(Title)),
            LinkHtml2 = binary:replace(LinkHtml1, <<"{{url}}">>, list_to_binary(NewLink)),
            LinkHtml2
        end, Children),
    LinkListHmtl = get(linklist_html),
    LinkListHmtl1 = binary:replace(LinkListHmtl, <<"{{links}}">>, iolist_to_binary(AllLinkHtml)),
    binary:replace(LinkListHmtl1, <<"{{links_title}}">>, links_title(BaseDir)).

links_title(BaseDir) ->
    [Lang|_] = string:tokens(BaseDir, "/"),
    maps:get(Lang, #{"zh-hans" => unicode:characters_to_binary("以下是本节中的文章："), "en" => <<"Here are the articles in this section:">>}).

make_relative_link(ParentLink, Link) ->
    PUrl = markdown_to_html_url(ParentLink),
    Url = markdown_to_html_url(Link),
    DirName = filename:dirname(PUrl),
    DirName = string:left(Url, length(DirName)),
    lists:sublist(Url, length(DirName)+2, length(Url)).

markdown_to_html_file(File) ->
    Bin = iolist_to_binary(File),
    Bin1 = binary:replace(Bin, <<"README.md">>, <<"index.html">>),
    Bin2 = binary:replace(Bin1, <<".md">>, <<".html">>),
    "_book/"++binary_to_list(Bin2).

markdown_to_html_url(File) ->
    Bin = iolist_to_binary(File),
    Bin1 = binary:replace(Bin, <<"README.md">>, <<"">>),
    Bin2 = binary:replace(Bin1, <<".md">>, <<".html">>),
    "_book/"++binary_to_list(Bin2).

parse_line(Line) ->
    {match, [[_, {TitleStart, TitleLen},{LinkStart, LinkLen}]]} = re:run(Line, "\\[(.*)\\]\\((.*)\\)", [global]),
    Title = string:substr(Line, TitleStart+1, TitleLen),
    Link = string:substr(Line, LinkStart+1, LinkLen),
    {Title, Link}.

get_children([Line|Lines], HeaderSize, Acc) ->
    NowHeaderSize = header_size(Line),
    case NowHeaderSize =< HeaderSize of
        true ->
            lists:reverse(Acc);
        false ->
            case NowHeaderSize == HeaderSize + 2 of
                true ->
                    get_children(Lines, HeaderSize, [Line|Acc]);
                false ->
                    get_children(Lines, HeaderSize, Acc)
            end
    end;
get_children([], _, Acc) ->
    lists:reverse(Acc).

header_size(Header) ->
    Prefix = lists:takewhile(fun(E)->E == $  orelse E == $* end, Header),
    case lists:member($*, Prefix) of
        false ->
            0;
        true ->
            length(Prefix)
    end.
