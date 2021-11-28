import json
import time
from statistics import mean
from typing import Callable

import simplejson

RUNS = 5
REPEATS = 100000

# Taken from https://www.json.org/example.html
DATA_EXAMPLES = [
    {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    },
    {
        "menu": {
            "id": "file",
            "value": "File",
            "popup": {
                "menuitem": [
                    {"value": "New", "onclick": "CreateNewDoc()"},
                    {"value": "Open", "onclick": "OpenDoc()"},
                    {"value": "Close", "onclick": "CloseDoc()"}
                ]
            }
        }
    },
    {
        "widget": {
            "debug": "on",
            "window": {
                "title": "Sample Konfabulator Widget",
                "name": "main_window",
                "width": 500,
                "height": 500
            },
            "image": {
                "src": "Images/Sun.png",
                "name": "sun1",
                "hOffset": 250,
                "vOffset": 250,
                "alignment": "center"
            },
            "text": {
                "data": "Click Here",
                "size": 36,
                "style": "bold",
                "name": "text1",
                "hOffset": 250,
                "vOffset": 100,
                "alignment": "center",
                "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
            }
        }
    },
    {
        "web-app": {
            "servlet": [
                {
                    "servlet-name": "cofaxCDS",
                    "servlet-class": "org.cofax.cds.CDSServlet",
                    "init-param": {
                        "configGlossary:installationAt": "Philadelphia, PA",
                        "configGlossary:adminEmail": "ksm@pobox.com",
                        "configGlossary:poweredBy": "Cofax",
                        "configGlossary:poweredByIcon": "/images/cofax.gif",
                        "configGlossary:staticPath": "/content/static",
                        "templateProcessorClass": "org.cofax.WysiwygTemplate",
                        "templateLoaderClass": "org.cofax.FilesTemplateLoader",
                        "templatePath": "templates",
                        "templateOverridePath": "",
                        "defaultListTemplate": "listTemplate.htm",
                        "defaultFileTemplate": "articleTemplate.htm",
                        "useJSP": False,
                        "jspListTemplate": "listTemplate.jsp",
                        "jspFileTemplate": "articleTemplate.jsp",
                        "cachePackageTagsTrack": 200,
                        "cachePackageTagsStore": 200,
                        "cachePackageTagsRefresh": 60,
                        "cacheTemplatesTrack": 100,
                        "cacheTemplatesStore": 50,
                        "cacheTemplatesRefresh": 15,
                        "cachePagesTrack": 200,
                        "cachePagesStore": 100,
                        "cachePagesRefresh": 10,
                        "cachePagesDirtyRead": 10,
                        "searchEngineListTemplate": "forSearchEnginesList.htm",
                        "searchEngineFileTemplate": "forSearchEngines.htm",
                        "searchEngineRobotsDb": "WEB-INF/robots.db",
                        "useDataStore": True,
                        "dataStoreClass": "org.cofax.SqlDataStore",
                        "redirectionClass": "org.cofax.SqlRedirection",
                        "dataStoreName": "cofax",
                        "dataStoreDriver": "com.microsoft.jdbc.sqlserver.SQLServerDriver",
                        "dataStoreUrl": "jdbc:microsoft:sqlserver://LOCALHOST:1433;DatabaseName=goon",
                        "dataStoreUser": "sa",
                        "dataStorePassword": "dataStoreTestQuery",
                        "dataStoreTestQuery": "SET NOCOUNT ON;select test='test';",
                        "dataStoreLogFile": "/usr/local/tomcat/logs/datastore.log",
                        "dataStoreInitConns": 10,
                        "dataStoreMaxConns": 100,
                        "dataStoreConnUsageLimit": 100,
                        "dataStoreLogLevel": "debug",
                        "maxUrlLength": 500}},
                {
                    "servlet-name": "cofaxEmail",
                    "servlet-class": "org.cofax.cds.EmailServlet",
                    "init-param": {
                        "mailHost": "mail1",
                        "mailHostOverride": "mail2"}},
                {
                    "servlet-name": "cofaxAdmin",
                    "servlet-class": "org.cofax.cds.AdminServlet"},

                {
                    "servlet-name": "fileServlet",
                    "servlet-class": "org.cofax.cds.FileServlet"},
                {
                    "servlet-name": "cofaxTools",
                    "servlet-class": "org.cofax.cms.CofaxToolsServlet",
                    "init-param": {
                        "templatePath": "toolstemplates/",
                        "log": 1,
                        "logLocation": "/usr/local/tomcat/logs/CofaxTools.log",
                        "logMaxSize": "",
                        "dataLog": 1,
                        "dataLogLocation": "/usr/local/tomcat/logs/dataLog.log",
                        "dataLogMaxSize": "",
                        "removePageCache": "/content/admin/remove?cache=pages&id=",
                        "removeTemplateCache": "/content/admin/remove?cache=templates&id=",
                        "fileTransferFolder": "/usr/local/tomcat/webapps/content/fileTransferFolder",
                        "lookInContext": 1,
                        "adminGroupID": 4,
                        "betaServer": True}}],
            "servlet-mapping": {
                "cofaxCDS": "/",
                "cofaxEmail": "/cofaxutil/aemail/*",
                "cofaxAdmin": "/admin/*",
                "fileServlet": "/static/*",
                "cofaxTools": "/tools/*"},

            "taglib": {
                "taglib-uri": "cofax.tld",
                "taglib-location": "/WEB-INF/tlds/cofax.tld"
            }
        }
    },
    {
        "menu": {
            "header": "SVG Viewer",
            "items": [
                {"id": "Open"},
                {"id": "OpenNew", "label": "Open New"},
                None,
                {"id": "ZoomIn", "label": "Zoom In"},
                {"id": "ZoomOut", "label": "Zoom Out"},
                {"id": "OriginalView", "label": "Original View"},
                None,
                {"id": "Quality"},
                {"id": "Pause"},
                {"id": "Mute"},
                None,
                {"id": "Find", "label": "Find..."},
                {"id": "FindAgain", "label": "Find Again"},
                {"id": "Copy"},
                {"id": "CopyAgain", "label": "Copy Again"},
                {"id": "CopySVG", "label": "Copy SVG"},
                {"id": "ViewSVG", "label": "View SVG"},
                {"id": "ViewSource", "label": "View Source"},
                {"id": "SaveAs", "label": "Save As"},
                None,
                {"id": "Help"},
                {"id": "About", "label": "About Adobe CVG Viewer..."}
            ]
        }
    }
]


def measure(method: Callable, args: tuple, repeats: int = REPEATS) -> int:
    start = time.perf_counter_ns()
    for _ in range(repeats):
        method(*args)
    return time.perf_counter_ns() - start


def measure_across_many(method: Callable,
                        args: tuple,
                        repeats: int = REPEATS,
                        runs: int = RUNS) -> tuple[int, float, int]:
    results = []
    for _ in range(runs):
        results.append(measure(method, args, repeats))

    return min(results), mean(results), max(results)


def print_result_for_measure_across_any(
        method_name: str,
        method: Callable,
        args: tuple,
        repeats: int = REPEATS,
        runs: int = RUNS
) -> None:
    min, avg, max = measure_across_many(method, args, repeats, runs)
    print(f"{method_name}: "
          f"{min/1000000000:3.3f}s / "
          f"{avg/1000000000:3.3f}s / "
          f"{max/1000000000:3.3f}s")


def benchmark_one_dict(data_set: dict):
    dumped_dict = json.dumps(data_set)
    print(f"Benchmarking: '{dumped_dict[:32]}...'")
    print_result_for_measure_across_any(
        "      json.dumps",
        json.dumps,
        (data_set,)
    )
    print_result_for_measure_across_any(
        "simplejson.dumps",
        simplejson.dumps,
        (data_set,)
    )
    print_result_for_measure_across_any(
        "      json.loads",
        json.loads,
        (dumped_dict,)
    )
    print_result_for_measure_across_any(
        "simplejson.loads",
        simplejson.loads,
        (dumped_dict,)
    )
    print()


def main():
    for data_set in DATA_EXAMPLES:
        benchmark_one_dict(data_set)

if __name__ == '__main__':
    main()

