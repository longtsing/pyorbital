Pyorbital
=========

Pyorbital 是一个 Python 包，用于根据 TLE 文件计算卫星的轨道参数，以及计算与卫星遥感相关的天文参数。
目前 Pyorbital 仅支持近地轨道卫星。


安装
------------

Pyorbital 可以通过 pip 从 Python 包索引（PyPI）或从 conda-forge conda 频道安装。要在现有环境中从 PyPI 安装：

.. code-block:: bash

   pip install pyorbital

或在现有的基于 conda 的环境中：

.. code-block:: bash

   conda install -c conda-forge pyorbital

从源代码安装
^^^^^^^^^^^

Pyorbital 也可以从源代码安装。如果您想从 GitHub 上的最新开发版本安装 pyorbital，可以运行：

.. code-block:: bash

   pip install git+https://github.com/pytroll/pyorbital.git

但是，如果您想编辑源代码并在运行代码时看到更改反映出来，可以克隆 git 仓库并以"可编辑"模式安装：

.. code-block:: bash

   git clone git://github.com/pytroll/pyorbital.git
   cd pyorbital
   pip install -e .


添加缺失的平台信息
--------------------------------

Pyorbital 附带一个 *platforms.txt* 文件，该文件将卫星名称映射到 NORAD 标识符。

此文件已经包含许多近地轨道环境或气象卫星，因此很可能足以满足您的需求。

但如果它不包含您感兴趣的卫星，请复制一份 `platforms.txt <https://github.com/pytroll/pyorbital/blob/main/pyorbital/etc/platforms.txt>`_
文件，添加缺失的卫星及其 NORAD 标识符，并将文件放置在由 :envvar:`PYORBITAL_CONFIG_PATH` 指向的目录中。

NORAD 标识符可以在两行元素文件中每行的第一个数字中找到（例如，从 `celestrak`_ 获取）。

Pyorbital 附带一个小脚本 ``check_platform.py`` 用于检查卫星是否已受支持。

.. code::

   python -m pyorbital.check_platform -s NOAA-21

   [INFO: 2023-01-22 21:20:25 : pyorbital.tlefile] Satellite NOAA-21 is supported. NORAD number: 54234
   [INFO: 2023-01-22 21:20:25 : pyorbital.tlefile] Satellite names and NORAD numbers are defined in /path/to/pyorbital/etc/directory/platforms.txt


TLE 文件
---------
Pyorbital 有一个用于解析 NORAD TLE 文件的模块

    >>> from pyorbital import tlefile
    >>> tle = tlefile.read('noaa 18', '/path/to/my/tle_file.txt')
    >>> tle.inclination
    99.043499999999995

如果未提供路径，pyorbital 首先尝试读取由环境变量 :envvar:`TLES` 定义的任何本地 TLE 文件，
该变量提供一个可用于检索所有相关文件的 glob 模式：

.. code::

   TLES=/path/to/tle_files/*/tle*txt

如果未设置此变量，Pyorbital 将尝试从 `celestrak`_ 通过互联网获取地球观测 TLE 文件。
请注意，仅当未提供特定 TLE 文件或未设置 :envvar:`TLES` 环境变量时，才会发生此下载。


TLE 下载和数据库
^^^^^^^^^^^^^^^^^^^^^^^^^

可以从 `celestrak 的请求页面 <https://celestrak.com/NORAD/archives/request.php>`_ 请求历史 TLE 文件。

还有一个脚本 ``fetch_tles.py``，可用于从多个位置收集 TLE 数据。当前支持的位置包括：

* 无需登录的通用网络位置
* Space-Track（需要登录凭据）
* 本地文件

数据保存在 SQLite3 数据库中，并可在每次运行后写入文件。要查看配置选项，请参阅 ``examples/tle.yaml`` 中的示例配置。

计算卫星位置
----------------------------
orbital 模块能够计算特定时间的卫星位置和速度：

    >>> from pyorbital.orbital import Orbital
    >>> import datetime as dt
    >>> # 使用来自互联网的当前 TLE：
    >>> orb = Orbital("Suomi NPP")
    >>> now = dt.datetime.now(dt.timezone.utc)
    >>> # 获取卫星的归一化位置和速度：
    >>> orb.get_position(now)
    (array([-0.20015267,  0.09001458,  1.10686756]),
     array([ 0.06148495,  0.03234914,  0.00846805]))
    >>> # 获取卫星的经度、纬度和高度：
    >>> orb.get_lonlatalt(now)
    (40.374855865574951, 78.849923885700363, 839.62504115338368)


使用实际 TLE 提高精度
------------------------------------

    >>> from pyorbital.orbital import Orbital
    >>> import datetime as dt
    >>> orb = Orbital("Suomi NPP")
    >>> dtobj = dt.datetime(2015,2,7,3,0)
    >>> orb.get_lonlatalt(dtobj)
    (152.11564698762811, 20.475251739329622, 829.37355785502211)

但由于我们感兴趣的是了解 Suomi-NPP 从现在起两年半多以后（2017 年 9 月 26 日）的位置，
我们不能依赖当前的 TLE，而是需要一个更接近感兴趣时间的 TLE：

    >>> snpp = Orbital('Suomi NPP', tle_file='/path/to/tle/files/tle-20150207.txt')
    >>> snpp.get_lonlatalt(dtobj)
    (105.37373804512762, 79.160752404540133, 838.94605490133154)

如果我们使用一周前的 TLE，会得到略有不同的结果：

    >>> snpp = Orbital('Suomi NPP', tle_file='/path/to/tle/files/tle-20150131.txt')
    >>> snpp.get_lonlatalt(dtobj)
    (104.1539184988462, 79.328272480878141, 838.81555967963391)



计算天文参数
---------------------------------
astronomy 模块能够计算卫星遥感感兴趣的某些参数，例如太阳天顶角：

    >>> from pyorbital import astronomy
    >>> import datetime as dt
    >>> utc_time = dt.datetime(2012, 5, 15, 15, 45)
    >>> lon, lat = 12, 56
    >>> astronomy.sun_zenith_angle(utc_time, lon, lat)
    62.685986438071602


.. envvar:: PYORBITAL_CONFIG_PATH

   可以（但不是强制）定义此环境变量，以完全控制 Pyorbital 使用的某些静态数据：

   Pyorbital 附带一个 *platforms.txt* 文件，该文件将卫星名称映射到 NORAD 标识符。
   此内部文件由 Pyorbital 访问，用户无需执行任何操作。但如果您需要更改或更新此文件，
   可以制作自己的副本并将其放置在此环境变量指向的目录中。

.. envvar:: TLES

   两行元素（TLE）文件可通过互联网自动访问，用户无需执行任何操作。
   这样做时，Pyorbital 将获取最新的 TLE 数据，但这对于历史数据等可能不是最佳选择。
   此外，在生产环境中可能不可持续。

   但是，可以通过指定此类本地 TLE 文件所在的位置，让 Pyorbital 在本地查找必要且更优的 TLE 数据。
   如果 TLES 环境变量设置为本地位置的 glob 模式，Pyorbital 将首先在那里搜索所需的 TLE。
   这在限制互联网访问的运营设置中以及处理旧/历史卫星数据时都很有用。

   可以（但不是强制）定义此环境变量。


API
---

轨道计算
^^^^^^^^^^^^^^^^^^^^

.. automodule:: pyorbital.orbital
   :members:
   :undoc-members:

TLE 处理
^^^^^^^^^^^^

.. automodule:: pyorbital.tlefile
   :members:
   :undoc-members:

天文计算
^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: pyorbital.astronomy
   :members:
   :undoc-members:


.. Contents:
   .. toctree::
      :maxdepth: 2
   索引和表格
   ==================
   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`



.. _celestrak: Celestrak <https://celestrak.com>
.. _github: http://github.com/pytroll/pyorbital
