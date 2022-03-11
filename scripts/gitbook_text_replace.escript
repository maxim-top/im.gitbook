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
