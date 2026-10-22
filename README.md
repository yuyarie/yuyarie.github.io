# Yuyarie 的个人网站

使用 HTML 与 CSS 构建，通过 GitHub Pages 发布。

网站地址：https://yuyarie.github.io

## 下载文件

把要分享的文件直接放到 `downloads/`，不需要子目录。这个目录只存资源，下载站页面和自动生成的列表放在 `downloadpage/`。页面会展示文件名、大小和下载按钮；隐藏文件和子目录不会列入下载列表。这里只放准备公开分享的文件。

```text
index.html                 网站主页
downloadpage/
  index.html               下载站页面
  files.json               自动生成的文件列表
downloads/
  .gitkeep                 保留空目录，不会显示在列表中
  工具.zip                  直接放入要分享的文件
scripts/
  build_downloads.py       生成文件列表
```

## 本地预览

添加或删除文件后，在项目根目录运行：

```powershell
python scripts/build_downloads.py
python -m http.server 8000
```

浏览器访问 http://localhost:8000。下载列表通过 HTTP 加载，不要直接双击下载页面预览。

## 发布

首次使用时，在仓库 **Settings → Pages → Build and deployment → Source** 中选择 **GitHub Actions**。

提交并推送到 `main` 后，工作流会自动扫描 `downloads/`、生成列表并发布网站，无需手动维护文件链接。仅首页、`downloadpage/` 和 `downloads/` 会发布。`downloadpage/files.json` 本地生成的变化可随文件一起提交，发布时也会重新生成。
