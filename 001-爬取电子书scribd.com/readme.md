## 第一步：需求分析
正在学习日语，小红书上发现这个形式挺好的。

<img src="static/小红书图片.jpg" width="300px">

才知道书名后，全网搜《用日本小学课本学50音图》这个本电子书，zlibrary上下载的不是很清晰，希望能够下一本全的。

## 第二步：谷歌搜索资源
发现scribd.com上面有

[scribd.com 用日本小学课本学50音图](https://www.scribd.com/document/665598179/%E7%94%A8%E6%97%A5%E6%9C%AC%E5%B0%8F%E5%AD%A6%E8%AF%BE%E6%9C%AC%E5%AD%A650%E9%9F%B3%E5%9B%BE-13583772 "scribd.com 用日本小学课本学50音图")

## 第三步：准备下载

下载订阅费用，但是在线可以浏览
<img src="static/下载要订阅要钱.png" width="600px">

说实话这些年就没存什么钱，大学辍学后，一直自己干，每月挣的里面，现在加上老婆那份，每月上供国家6k+。

<img src="static/在线能浏览第一页.png" width="600px">

在线能浏览第一页

<img src="static/在线能浏览最后一页.png" width="600px">

在线能浏览最后一页

## 第四步：开始破解
开始找DOM层位置

<img src="static/通过审查元素Elements找到图片.jpg" width="600px">

常规操作，直接右键审查元素，发现位置是图片，有链接。

<img src="static/通过network找到208的位置.jpg" width="600px">

通过network找图片地址里面的字符串，优先找了208，发现页面有渲染部分。

## 第五步：web控制台验证
```
docManager.pages
```
<img src="static/web控制台验证.png" width="600px">

直接使用 docManager.pages 发现可以拿到列表

```
pages_list = []
a=docManager.pages
for (i in a){
    pages_list.push(a[i]["contentUrl"])
}

# 打印成果
console.log(pages_list)

# 为了后面爬取方便转字符串使用
console.log(JSON.stringify(pages_list))
```

<img src="static/JS脚本拿到.jpg" width="600px">

脚本拿到链接地址。

```
# 脚本获取列表地址
https://html.scribdassets.com/95s13rsbwgbc5wff/pages/1-cd9be67960.jsonp

# 图片真实地址
https://html.scribdassets.com/95s13rsbwgbc5wff/images/1-cd9be67960.jpg
```

## 第六步：使用Python大法



