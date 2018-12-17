# webpy 代码框架

## 路由

默认路由映射规则是:

    `/<module>/<action>` 位于 `controllers/<module>.py` 中的 class <Action>

其中 module 和 action 是连字符拼接而成，且字母都会转换成小写。

例如：

* `/site/login` 位于 `controllers/Site.py` 中的 class Login
* `/test/hello-world` 位于 `controllers/Test.py` 中的 class HelloWorld

如果对于某个类，期望使用自定义的 url ，可在该类中定义一个 url 变量，例如 `controllers/Site.py`：

    class Index:
        url = '/'
        def GET(self):
            return 'Hello World!\n'

框架会将 `/` 映射到上述代码。

## 配置

开发环境配置位于 `config/dev.py` ，可以使用 `config/local.py` 覆盖。注：local.py 已列入 .gitignore，不应被提交到git。

生产环境配置位于 `config/production.py` 。

默认使用开发环境配置，在生产环境中，可修改 WEBPYENV 环境变量为 production 。

也可以修改 `config/__init__.py` 中的判断方式。

## 常量

全局共享常量应当放置于 `const/__init__.py`

某个数据库字段的定义值，应当放在对应的 model 文件中，参考 `models/Apply.py`

## 数据库

数据库 ORM 使用 sqlalchemy ，默认没有自动提交；如有需要，可修改 code.py 开启（不建议开启）

具体使用，参考 `controllers/user.py` 和 `models/User.py`

## 日志

`from libraries import log` 引入日志模块以后，即可使用 logging 的 debug、info、warning、error、critical 这5个方法。参考 `controllers/Test.py` 。


## 测试

测试代码应当位于 `tests/` 目录下。

