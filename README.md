# 5zipai
爬取网页图片，以标题创建本地文件夹并且通过selenium以及autoit将爬取到的文件自动上传到微云中


本次爬取遇到的问题：

1.由于是墙外网站，所以打算是用无界将整个计算机网络进行代理，但是由于代理软件会把端口改掉，导致python报出ssl错误；
  解决办法：1）将证书更新
           2）将verify设置为False
           3）更改端口
  解决过程：使用以上方法均没有效果，而且在csdn中遇到相同翻墙后报ssl错误，最终将爬取目标链接改为国内镜像网站，不开代理，问题解决。
  
2.变量命名习惯不好，用相同的名字命名，导致在循环结构中不断累加，导致文件名字出错；

3.在selenium自动化测试中，出现通过xpath找不到元素，但是在chrome中能够搜索到；
  解决办法：后通过查找原因，发现网页中存在iframe框，导致selenium无法找到指定元素，而通过switch_to.frame('id'|'name'|'others')，当然起初使用
  switch_to_frame,原因是它被后来的Python版本所抛弃。

4.selenium无法控制Windows窗口；
  解决办法：通过autoit脚本文件实现对窗口的控制，将脚本利用自带的软件转为exe文件，通过os模块调用exe文件。