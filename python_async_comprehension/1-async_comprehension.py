#!/usr/bin/env python3
"""
"""

async_generator = __import__("0-async_generator").async_generator

async def async_generator ():
    num_ten = [i async for i in async_generator()] 
    return num_ten