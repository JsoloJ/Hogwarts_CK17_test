接口测试框架

编写框架思路：

1、从一个简单demo做起，什么都不用考虑，先实现一个接口的请求，调试各种请求方法和参数的格式

2、将每次都需要传入的固定参数放在base_api中，比如像获取token、cookie，以及发送请求方法都封装在其中

3、将每个接口抽离，比如用户处理这一大类的接口都放在一个业务接口页面，如我这里的user_api，其中放入
这一大类型的所有接口，这个接口中需要做数据的处理的，以及后续可能用到的数据的返回。

4、编写一个测试用例，调用对应这个user_api中的接口，如创建用户的用例就调用创建用户接口的封装法法

5、将测试数据抽离，放到一个数据驱动文件中，我这里选择的excel文件，主要是为了方便使用，后续优化准备
逐步放到yaml文件中

6、编写工具方法来读取测试数据、写入结果数据，我这里都放在util中

7、将读出的数据传入测试用例当中

8、因原始数据不方便入参，还需要将数据进一步处理和提取，这里在baseapi中进行了数据分流处理
将不同请求的方式的数据进行不同的组装，这里需要考虑灵活处理，不能写死，这样也可以为后续
不同请求方法预留接口

9、将处理好的数据返回到user_api（后续叫page_api）的对应接口当中，在page_api中调用baseapi的
请求方法，发送请求，最后返回请求数据、传入测试数据（返回传入测试数据主要是为了后续可能需要用到
用作断言，或者流程测试用例中的数据复用）、用作断言的预期结果、以及需要写入excel中的执行结果的
行号。

10、测试用例中将返回的数据进行接收，然后需要断言和数据写入


需要优化：

TODO1：需要优化测试数据，加入期望结果、实际结果、执行结果；并将实际结果和执行结果写入 -----done

TODO2：需要加入测试报告 allure feature story step （UI测试还可以加入截图、视屏等）------done

TODO3：需要加入日志系统    ------done

TODO4：需要优化token数据管理、加入配置文件，将所有文件放入系统配置文件，包含路径、sheetname名字   ------done

TODO5: 需要将case、page中重复代码全部封装  ------done

TODO6：需要考虑如果真实项目没有获取token这一步骤需要灵活调整，预留一个接口

TODO7:控制用例的运行顺序,标注执行参数

后期规划：

TODO1：将所有测试用例收集执行，生成测试报告，在本地使用服务管理测试报告（tomcat+jenkins)

TODO2：使用jenkins定制执行测试

TODO3：加入邮件发送

TODO4: 搭建数据存储系统，使用mysql或者uxdb等数据库管理信息

TODO5: 开发sdk，规范接口，输入接口示例数据，自动生成基础测试数据，简化测试用例设计

------------------------------基线化------------------------------------

文件内容解释：
business:业务代码，业务的各种接口方法都放在其中
config:配置文件，主要存放一些系统变量，放在一起方便管理
data:测试数据，建议一个接口放一个sheet,一个模块放一个文件
log:执行测试产生的日志信息
result_report:执行结果和报告
testcases:测试用例
util:工具
requirements.txt：项目需要的python三方库


环境：
环境搭建：https://jingyan.baidu.com/article/6b97984d7e55c85da3b0bf48.html
安装python、安装java环境
下载allure,并配置环境变量，下载地址：https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/
下载pycharm,然后新建一个项目，设置file--setting--project interpreter，选择python环境
安装requirements中的python三方库
设置file--setting -- tools --python integrated Tools 将unittest换成pytest
然后新建一个以test开都的函数就可以执行了
注意：pytest的命名规则基本都是以test开头，类名首字母大写

