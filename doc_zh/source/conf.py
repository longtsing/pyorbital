# -*- coding: utf-8 -*-
#
# pyorbital 文档构建配置文件，由以下命令创建：
# sphinx-quickstart on Mon Oct  3 08:48:29 2011.
#
# 此文件在其所在目录中通过 execfile() 执行。
#
# 请注意，并非所有可能的配置值都出现在这个
# 自动生成的文件中。
#
# 所有配置值都有一个默认值；注释掉的值
# 用来显示默认值。
"""Sphinx 文档构建配置。"""

import datetime as dt
import os
import sys

# 如果扩展（或使用 autodoc 记录的模块）在另一个目录中，
# 请在此处将这些目录添加到 sys.path。如果目录相对于
# 文档根目录，请使用 os.path.abspath 使其成为绝对路径，如下所示。

sys.path.insert(0, os.path.abspath("../../"))
sys.path.insert(0, os.path.abspath("../../pyorbital"))
from pyorbital.version import __version__  # noqa

# -- 常规配置 -----------------------------------------------------

# 如果您的文档需要最低 Sphinx 版本，请在此处声明。
# #needs_sphinx = '1.0'

# 在此处添加任何 Sphinx 扩展模块名称，以字符串形式。它们可以是
# Sphinx 附带的扩展（名为 'sphinx.ext.*'）或您自定义的扩展。
extensions = ["sphinx.ext.autodoc", "sphinx.ext.doctest", "sphinx.ext.coverage", "sphinx.ext.napoleon"]

# 在此处添加包含模板的任何路径，相对于此目录。
templates_path = [".templates"]

# 源文件名的后缀。
source_suffix = ".rst"

# 源文件的编码。
# #source_encoding = 'utf-8-sig'

# 主 toctree 文档。
master_doc = "index"

# 有关项目的常规信息。
project = u"pyorbital"
copyright = u"2012, 2024-{}, PyTroll 团队".format(dt.datetime.utcnow().strftime("%Y"))  # noqa: A001



# 您正在记录的项目的版本信息，用作
# |version| 和 |release| 的替换，也在
# 构建文档的各个其他地方使用。
#
# 简短的 X.Y 版本。
version = __version__.split("+")[0]
# 完整版本，包括 alpha/beta/rc 标签。
release = __version__

# Sphinx 自动生成内容的语言。有关
# 支持的语言列表，请参阅文档。
language = "zh_CN"

# 有两个选项可用于替换 |today|：要么设置 today 为某个
# 非 false 值，然后使用它：
# #today = ''
# 否则，today_fmt 用作 strftime 调用的格式。
# #today_fmt = '%B %d, %Y'

# 相对于源目录的模式列表，用于匹配在查找源文件时
# 要忽略的文件和目录。
# exclude_patterns = []

# 用于所有文档的 reST 默认角色（用于此标记：`text`）。
# #default_role = None

# 如果为 true，则会在 :func: 等交叉引用文本后附加 '()'。
# #add_function_parentheses = True

# 如果为 true，则当前模块名称将添加到所有描述
# 单元标题的前面（例如 .. function::）。
# #add_module_names = True

# 如果为 true，则 sectionauthor 和 moduleauthor 指令将显示在
# 输出中。默认情况下它们会被忽略。
# show_authors = False

# 要使用的 Pygments（语法高亮）样式的名称。
pygments_style = "sphinx"

# 模块索引排序的忽略前缀列表。
# #modindex_common_prefix = []


# -- HTML 输出选项 ---------------------------------------------------

# 用于 HTML 和 HTML 帮助页面的主题。Sphinx 附带的主要主题
# 目前是 'default' 和 'sphinxdoc'。
html_theme = "sphinx_rtd_theme"

# 主题选项是特定于主题的，用于进一步自定义主题的外观。
# 有关每个主题可用选项的列表，请参阅
# 文档。
# #html_theme_options = {}

# 在此处添加包含自定义主题的任何路径，相对于此目录。
# #html_theme_path = []

# 此 Sphinx 文档集的名称。如果为 None，则默认为
# "<project> v<release> 文档"。
# #html_title = None

# 导航栏的较短标题。默认值与 html_title 相同。
# #html_short_title = None

# 图像文件的名称（相对于此目录），放置在
# 侧边栏的顶部。
# #html_logo = None

# 图像文件的名称（在静态路径内），用作文档的网站图标。
# 此文件应为 Windows 图标文件（.ico），大小为 16x16 或 32x32
# 像素。
# #html_favicon = None

# 在此处添加包含自定义静态文件（例如样式表）的任何路径，
# 相对于此目录。它们在内置静态文件之后复制，
# 因此名为 "default.css" 的文件将覆盖内置的 "default.css"。
html_static_path = ["_static"]

html_css_files = [
    "theme_overrides.css",  # 覆盖 RTD 主题中的宽表格
    "https://cdn.datatables.net/1.10.23/css/jquery.dataTables.min.css",
]

html_js_files = [
    "https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js",
    "main.js",
]


# 如果不为 ''，则在每个页面底部插入 'Last updated on:' 时间戳，
# 使用给定的 strftime 格式。
# #html_last_updated_fmt = '%b %d, %Y'

# 如果为 true，则 SmartyPants 将用于将引号和破折号转换为
# 排版正确的实体。
# #html_use_smartypants = True

# 自定义侧边栏模板，将文档名称映射到模板名称。
# #html_sidebars = {}

# 应呈现到页面的其他模板，将页面名称映射到
# 模板名称。
# #html_additional_pages = {}

# 如果为 false，则不生成模块索引。
# #html_domain_indices = True

# 如果为 false，则不生成索引。
# #html_use_index = True

# 如果为 true，则索引将拆分为每个字母的单独页面。
# #html_split_index = False

# 如果为 true，则将 reST 源的链接添加到页面。
# #html_show_sourcelink = True

# 如果为 true，则在 HTML 页脚中显示 "Created using Sphinx"。默认为 True。
# #html_show_sphinx = True

# 如果为 true，则在 HTML 页脚中显示 "(C) Copyright ..."。默认为 True。
# #html_show_copyright = True

# 如果为 true，则将输出 OpenSearch 描述文件，并且所有页面将
# 包含引用它的 <link> 标签。此选项的值必须是
# 提供完成的 HTML 的基本 URL。
# #html_use_opensearch = ''

# 这是 HTML 文件的文件名后缀（例如 ".xhtml"）。
# #html_file_suffix = None

# HTML 帮助构建器的输出文件基本名称。
htmlhelp_basename = "pyorbitaldoc"


# -- LaTeX 输出选项 --------------------------------------------------

# 纸张大小（'letter' 或 'a4'）。
# #latex_paper_size = 'letter'

# 字体大小（'10pt'、'11pt' 或 '12pt'）。
# #latex_font_size = '10pt'

# 将文档树分组为 LaTeX 文件。元组列表
# （源起始文件，目标名称，标题，作者，文档类 [howto/manual]）。
latex_documents = [
    ("index", "pyorbital.tex", u"pyorbital 文档",
     u"Pytroll 团队", "manual"),
]

# 图像文件的名称（相对于此目录），放置在
# 标题页的顶部。
# #latex_logo = None

# 对于 "manual" 文档，如果为 true，则顶级标题是部分，
# 而不是章节。
# #latex_use_parts = False

# 如果为 true，则在内部链接后显示页面引用。
# #latex_show_pagerefs = False

# 如果为 true，则在外部链接后显示 URL 地址。
# #latex_show_urls = False

# LaTeX 前导码的附加内容。
# #latex_preamble = ''

# 要作为附录附加到所有手册的文档。
# #latex_appendices = []

# 如果为 false，则不生成模块索引。
# #latex_domain_indices = True


# -- 手册页输出选项 --------------------------------------------

# 每个手册页一个条目。元组列表
# （源起始文件，名称，描述，作者，手册部分）。
man_pages = [
    ("index", "pyorbital", u"pyorbital 文档",
     [u"Pytroll 团队"], 1)
]
