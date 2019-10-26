# -*- coding: utf-8 -*-
"""Webex Teams Access-Tokens API wrapper.

Copyright (c) 2016-2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from .abstract_components import Serializable

class Container(Serializable):
    def __init__(self, items, selectAction=None,
                              style=None,
                              verticalContentAlignment=None,
                              height=None,
                              separator=None,
                              spacing=None,
                              id=None):
        self.type = "Container"
        self.items = items
        self.selectAction = selectAction
        self.style = style
        self.verticalContentAlignment = verticalContentAlignment
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id

        super().__init__(serializable_properties=['items'],
                         simple_properties=[
                            'selectAction', 'style', 'verticalContentAlignment',
                            'height', 'separator', 'spacing', 'id', 'type'
                         ])

class ColumnSet(Serializable):
    def __init__(self, columns=None,
                       selectAction=None,
                       height=None,
                       separator=None,
                       spacing=None,
                       id=None):
        self.type = "ColumnSet"
        self.columns = columns
        self.selectAction = selectAction
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id

        super().__init__(serializable_properties=['columns'],
                         simple_properties=[
                            'selectAction', 'height', 'separator', 'spacing',
                            'id', 'type'
                         ])

class FactSet(Serializable):
    def __init__(self, facts, height=None,
                              separator=None,
                              spacing=None,
                              id=None):
        self.type = "FactSet"
        self.facts = facts
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id

        super().__init__(serializable_properties=['facts'],
                         simple_properties=[
                            'type', 'height', 'separator', 'id', 'spacing'
                         ])

class ImageSet(Serializable):
    def __init__(self, images, imageSize=None,
                               height=None,
                               separator=None,
                               spacing=None,
                               id=None):
        self.type = "ImageSet"
        self.images = images
        self.imageSize = imageSize
        self.height = height
        self.separator = separator
        self.spacing = spacing
        self.id = id

        super().__init__(serializable_properties=['images'],
                         simple_properties=[
                            'imageSize', 'height', 'separator', 'spacing', 'id',
                            'type'
                        ])
