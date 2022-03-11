#!/usr/bin/env escript
%% -*- mode: erlang;erlang-indent-level: 4;indent-tabs-mode: nil -*-
%% ex: ft=erlang ts=4 sw=4 et
main(_Args) ->
    Files = filelib:wildcard("_book/**/*.html"),
    Rules = [{<<"&#x672C;&#x4E66;&#x4F7F;&#x7528; GitBook &#x53D1;&#x5E03;">>, unicode:characters_to_binary("本文档由 Gitbook 发布")},
            {<<"all right reserved&#xFF0C;powered by Gitbook">>, <<>>}],
    lists:foreach(
        fun(File) ->
            {ok, Bin} = file:read_file(File),
            NewBin = lists:foldl(
                fun({OriginText, ReplaceText}, Acc) ->
                    binary:replace(Acc, OriginText, ReplaceText)
                end, Bin, Rules),
            case Bin /= NewBin of
                true ->
                    file:write_file(File, NewBin);
                false ->
                    skip
            end
        end, Files),
    ok.

% replace_html_code(Bin) ->
%     replace_html_code(binary_to_list(Bin), [], []).

% replace_html_code([$&|Rest], Now, Acc) ->
%     replace_html_code(Rest, [$&], [Now|Acc]);
% replace_html_code([$#|Rest], [$&], Acc) ->
%     replace_html_code(Rest, [$&,$#], Acc);
% replace_html_code([$;|Rest], [$&,$#|_]=Now, Acc) ->
%     replace_html_code(Rest, [], [html_code(Now)|Acc]);
% replace_html_code([C|Rest], [$&,$#|_]=Now, Acc) when C >= $0 andalso C =< $9 ; C >= $A andalso C =< $F; C == $x ->
%     replace_html_code(Rest, Now++[C], Acc);
% replace_html_code([C|Rest], [], Acc) ->
%     replace_html_code(Rest, [], [C|Acc]);
% replace_html_code([C|Rest], Now, Acc) ->
%     replace_html_code(Rest, [], [C,Now|Acc]);
% replace_html_code([], [], Acc) ->
%     iolist_to_binary(lists:reverse(Acc)).

% html_code([$&, $#, $x | Rest]=E) ->
%     I = list_to_integer(Rest, 16),
%     case I > 128 of
%         true ->
%             unicode:characters_to_binary([I]);
%         false ->
%             iolist_to_binary(E)
%     end.
