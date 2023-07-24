BASE_URL = "https://github.com/SamQxd"
path = r"D:\download\selenium"
repositories_tab = 'a[href*="/SamQxd?tab=repositories"]'
repositories_list = 'a[itemprop*="name codeRepository"]'
repository_id =  'return document.querySelector(\'meta[name="octolytics-dimension-repository_id"]\').getAttribute("content");'
download_button = 'summary[data-hydro-click*="repository.click"][data-view-component="true"]'
account = 'a[href*="/SamQxd"]'
