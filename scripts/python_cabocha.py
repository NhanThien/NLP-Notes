#!/usr/bin/python
# -*- coding: utf-8 -*-

import CaboCha
c = CaboCha.Parser()

sentence = "太郎はこの本を渡した。"

tree =  c.parse(sentence)

for i in range(tree.chunk_size()):
    chunk = tree.chunk(i)
    print( 'Chunk:', i)
    print( ' Score:', chunk.score)
    print( ' Link:', chunk.link)
    print( ' Size:', chunk.token_size )
    print( ' Pos:', chunk.token_pos )
    print( ' Head:', chunk.head_pos ) # 主辞
    print( ' Func:', chunk.func_pos ) # 機能語
    print( ' Features:', )
    for j in range(chunk.feature_list_size):
        print( chunk.feature_list(j) )
    print()
    print()

for i in range(tree.token_size()):
    token = tree.token(i)
    print( 'Surface:', token.surface )
    print( ' Normalized:', token.normalized_surface )
    print( ' Feature:', token.feature )
    print( ' NE:', token.ne ) # 固有表現
    print( ' Info:', token.additional_info )
    print( ' Chunk:', token.chunk )
    print()
