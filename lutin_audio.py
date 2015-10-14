#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_type():
	return "LIBRARY"

def get_desc():
	return "Basic audio types"

def get_licence():
	return "APACHE-2"

def get_compagny_type():
	return "com"

def get_compagny_name():
	return "atria-soft"

def get_maintainer():
	return ["Mr DUPIN Edouard <yui.heero@gmail.com>"]

def get_version():
	return [0,1]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
		'audio/debug.cpp',
		'audio/channel.cpp',
		'audio/format.cpp',
		'audio/Time.cpp',
		'audio/Duration.cpp',
		'audio/int8_8_t.cpp',
		'audio/int8_16_t.cpp',
		'audio/int16_16_t.cpp',
		'audio/int16_32_t.cpp',
		'audio/int24_24_t.cpp',
		'audio/int24_32_t.cpp',
		'audio/int32_32_t.cpp',
		'audio/int32_64_t.cpp',
		'audio/int64_64_t.cpp',
		'audio/float_t.cpp',
		'audio/double_t.cpp'
		])
	my_module.add_header_file([
		'audio/types.h',
		'audio/debug.h',
		'audio/debugRemove.h',
		'audio/channel.h',
		'audio/format.h',
		'audio/Time.h',
		'audio/Duration.h',
		'audio/int8_8_t.h',
		'audio/int8_16_t.h',
		'audio/int16_16_t.h',
		'audio/int16_32_t.h',
		'audio/int24_24_t.h',
		'audio/int24_32_t.h',
		'audio/int32_32_t.h',
		'audio/int32_64_t.h',
		'audio/int64_64_t.h',
		'audio/float_t.h',
		'audio/double_t.h'
		])
	my_module.add_module_depend(['etk'])
	my_module.add_path(tools.get_current_path(__file__))
	return my_module

