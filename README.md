这是一个支持HTTPs的web server。

主要优点：
（1）Server的配置都是通过配置文件来设定的，例如对于https://10.10.10.10/esrs/unity/FSN34946723M/keepalive这个URL，
它的返回信息在keepalive.json文件里，如果需要更改它的返回内容直接更改即可，#表示该内容会被替换，替换的顺序是URL-> head -> body。
（2）实现全局object来处理不同的请求，在程序一开始运行时就生成了全局的object。
（3）匹配的URL使用的是正则表达式，如果可以匹配上则从URL中取出SN并生成Dic。
