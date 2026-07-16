# SonarQube 问题分档

来源：`D:\AIbot\nb2\mlbot\koinoribot-sonarqube-report.md`
生成说明：逐条保留 SonarQube 报告中的 Issue 与 Security Hotspot，并按修复优先级分为三档。

## 汇总

| 分档 | 数量 | 处理建议 |
|---|---:|---|
| 建议修复 | 55 | 优先纳入近期修复，尤其是 Bug、异常处理、恒定条件、HTTP 与验证码随机数。 |
| 可选修复 | 113 | 适合作为低风险清理或随相关功能改动顺手处理。 |
| 建议保留 | 101 | 多数为误报或环境/业务取舍；建议在 SonarQube 中确认并标记。 |

## 分档依据

- 建议修复：可能影响行为、安全、异常处理，或复杂度已明显妨碍维护。
- 可选修复：主要是样式、清理、低风险重构；可在不影响业务节奏时处理。
- 建议保留：当前更像 Sonar 规则偏好或安全热点误报；保留前仍建议人工确认上下文。

## 建议修复

共 55 条。

| # | 类型 | 严重程度 | 文件 | 行号 | 规则 | 问题 | 分档理由 |
|---:|---|---|---|---:|---|---|---|
| 1 | Security Hotspot | `低（LOW）` | `plugins/public_whitelist/__init__.py` | 189 | `python:S5332` | Using http protocol is insecure. Use https instead | HTTP 明文传输热点，若外部访问可被劫持；优先改 HTTPS 或明确内部地址例外。 |
| 2 | Security Hotspot | `低（LOW）` | `plugins/public_whitelist/__init__.py` | 189 | `python:S5332` | Using http protocol is insecure. Use https instead | HTTP 明文传输热点，若外部访问可被劫持；优先改 HTTPS 或明确内部地址例外。 |
| 3 | Security Hotspot | `中（MEDIUM）` | `uid_manager.py` | 326 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 用于生成绑定验证码，应改用 secrets 等安全随机数。 |
| 4 | Security Hotspot | `中（MEDIUM）` | `uid_manager.py` | 329 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 用于生成绑定验证码，应改用 secrets 等安全随机数。 |
| 5 | Issue | 严重（CRITICAL） | `build_image.py` | 116 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 61 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 6 | Issue | 严重（CRITICAL） | `build_image.py` | 212 | `python:S5754` | Specify an exception class to catch or reraise the exception | 裸 except 会吞掉退出/中断等异常，建议限定异常类型。 |
| 7 | Issue | 严重（CRITICAL） | `build_image.py` | 234 | `python:S5797` | Replace this expression; used as a condition it will always be constant. | 条件恒定，容易造成不可达分支或误判。 |
| 8 | Issue | 严重（CRITICAL） | `build_image.py` | 250 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 9 | Issue | 严重（CRITICAL） | `build_image.py` | 252 | `python:S5797` | Replace this expression; used as a condition it will always be constant. | 条件恒定，容易造成不可达分支或误判。 |
| 10 | Issue | 主要（MAJOR） | `build_image.py` | 571 | `python:S112` | Replace this generic exception class with a more specific one. | 抛出过泛异常，不利于调用方精准处理。 |
| 11 | Issue | 严重（CRITICAL） | `build_image.py` | 910 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 19 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 12 | Issue | 严重（CRITICAL） | `plugins/ai_draw/__init__.py` | 267 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 36 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 13 | Issue | 严重（CRITICAL） | `plugins/ai_draw/_image_response.py` | 47 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 14 | Issue | 严重（CRITICAL） | `plugins/call_me_please/__init__.py` | 54 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 21 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 15 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 177 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 19 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 16 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 433 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 17 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 474 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 24 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 18 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 492 | `python:S5754` | Specify an exception class to catch or reraise the exception | 裸 except 会吞掉退出/中断等异常，建议限定异常类型。 |
| 19 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 1193 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 19 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 20 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 157 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 33 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 21 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 716 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 29 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 22 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 814 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 22 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 23 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 866 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 20 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 24 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 1053 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 24 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 25 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 1118 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 31 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 26 | Issue | 严重（CRITICAL） | `plugins/english_guess/__init__.py` | 132 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 19 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 27 | Issue | 严重（CRITICAL） | `plugins/english_guess/__init__.py` | 398 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 28 | Issue | 主要（MAJOR） | `plugins/english_guess/__init__.py` | 401 | `python:S5869` | Remove duplicates in this character class. | 正则字符类重复，容易掩盖表达式意图错误。 |
| 29 | Issue | 严重（CRITICAL） | `plugins/english_guess/__init__.py` | 477 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 28 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 30 | Issue | 严重（CRITICAL） | `plugins/english_guess/__init__.py` | 560 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 31 | Issue | 严重（CRITICAL） | `plugins/english_guess/get_hint.py` | 5 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 31 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 32 | Issue | 严重（CRITICAL） | `plugins/english_guess/guess_func.py` | 30 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 33 | Issue | 严重（CRITICAL） | `plugins/feisheng/__init__.py` | 264 | `python:S5754` | Specify an exception class to catch or reraise the exception | 裸 except 会吞掉退出/中断等异常，建议限定异常类型。 |
| 34 | Issue | 严重（CRITICAL） | `plugins/feisheng/__init__.py` | 394 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 20 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 35 | Issue | 严重（CRITICAL） | `plugins/feisheng/__init__.py` | 484 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 18 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 36 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 625 | `python:S3923` | Remove this if statement or edit its code blocks so that they're not all the same. | Bug：if 分支行为相同，可能是条件或分支实现写错。 |
| 37 | Issue | 严重（CRITICAL） | `plugins/fishing/getfish.py` | 126 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 34 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 38 | Issue | 严重（CRITICAL） | `plugins/fishing/getfish.py` | 221 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 55 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 39 | Issue | 严重（CRITICAL） | `plugins/fishing/util.py` | 108 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 21 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 40 | Issue | 严重（CRITICAL） | `plugins/hongbao/__init__.py` | 87 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 41 | Issue | 严重（CRITICAL） | `plugins/icelogin/__init__.py` | 203 | `python:S5754` | Specify an exception class to catch or reraise the exception | 裸 except 会吞掉退出/中断等异常，建议限定异常类型。 |
| 42 | Issue | 主要（MAJOR） | `plugins/icelogin/__init__.py` | 329 | `python:S1871` | Either merge this branch with the identical one on line "327" or change one of the implementations. | 重复分支通常表示遗漏了差异化逻辑。 |
| 43 | Issue | 严重（CRITICAL） | `plugins/icelogin/__init__.py` | 577 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 34 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 44 | Issue | 主要（MAJOR） | `plugins/icelogin/__init__.py` | 604 | `python:S1871` | Either merge this branch with the identical one on line "600" or change one of the implementations. | 重复分支通常表示遗漏了差异化逻辑。 |
| 45 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 114 | `python:S5754` | Specify an exception class to catch or reraise the exception | 裸 except 会吞掉退出/中断等异常，建议限定异常类型。 |
| 46 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 170 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 99 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 47 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 313 | `python:S5754` | Specify an exception class to catch or reraise the exception | 裸 except 会吞掉退出/中断等异常，建议限定异常类型。 |
| 48 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 512 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 39 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 49 | Issue | 严重（CRITICAL） | `plugins/public_whitelist/__init__.py` | 511 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 50 | Issue | 严重（CRITICAL） | `plugins/shaojo/__init__.py` | 88 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 51 | Issue | 严重（CRITICAL） | `plugins/shaojo/choicer.py` | 28 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 18 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 52 | Issue | 严重（CRITICAL） | `plugins/shaojo/choicer.py` | 84 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 53 | Issue | 严重（CRITICAL） | `tools.py` | 145 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 54 | Issue | 严重（CRITICAL） | `tools.py` | 177 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 70 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |
| 55 | Issue | 严重（CRITICAL） | `tools.py` | 404 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 88 to the 15 allowed. | 认知复杂度过高，后续改动和排错成本较高；可拆分小函数。 |

## 可选修复

共 113 条。

| # | 类型 | 严重程度 | 文件 | 行号 | 规则 | 问题 | 分档理由 |
|---:|---|---|---|---:|---|---|---|
| 1 | Issue | 主要（MAJOR） | `build_image.py` | 14 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 2 | Issue | 主要（MAJOR） | `build_image.py` | 117 | `python:S107` | Method "__init__" has 16 parameters, which is greater than the 13 authorized. | 参数较多影响可读性；若构造调用稳定，可暂缓到重构时处理。 |
| 3 | Issue | 次要（MINOR） | `build_image.py` | 184 | `python:S116` | Rename this field "markImg" to match the regular expression ^[_a-z][_a-z0-9]*$. | 命名风格问题；若涉及外部字段或历史数据，改名前需确认兼容。 |
| 4 | Issue | 严重（CRITICAL） | `build_image.py` | 269 | `python:S1192` | Define a constant instead of duplicating this literal "center_type must be 'center', 'by_width' or 'by_height'" 3 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 5 | Issue | 主要（MAJOR） | `build_image.py` | 499 | `python:S1172` | Remove the unused function parameter "center_type". | 未使用参数可清理；若是框架/回调签名需保留。 |
| 6 | Issue | 次要（MINOR） | `build_image.py` | 892 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 7 | Issue | 次要（MINOR） | `money.py` | 35 | `python:S7508` | Remove this redundant call. | 冗余调用可删除，低风险清理。 |
| 8 | Issue | 次要（MINOR） | `plugins/ai_draw/_image_response.py` | 87 | `python:S5713` | Remove this redundant Exception class; it derives from another which is already caught. | 重复捕获异常类可清理，需确认异常处理顺序。 |
| 9 | Issue | 主要（MAJOR） | `plugins/call_me_please/__init__.py` | 82 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 10 | Issue | 主要（MAJOR） | `plugins/call_me_please/__init__.py` | 91 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 11 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 192 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 12 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 202 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 13 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 212 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 14 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 224 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 15 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 629 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 16 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 784 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 17 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 836 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 18 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 989 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 19 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 996 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 20 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 1018 | `python:S7519` | Replace with dict fromkeys method call | 可用 dict.fromkeys 简化，属于可读性优化。 |
| 21 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 1044 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 22 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 1181 | `python:S1192` | Define a constant instead of duplicating this literal "金额必须是数字！" 5 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 23 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 1199 | `python:S5713` | Remove this redundant Exception class; it derives from another which is already caught. | 重复捕获异常类可清理，需确认异常处理顺序。 |
| 24 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 1199 | `python:S5713` | Remove this redundant Exception class; it derives from another which is already caught. | 重复捕获异常类可清理，需确认异常处理顺序。 |
| 25 | Issue | 主要（MAJOR） | `plugins/chaogu/stock_utils.py` | 1 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 26 | Issue | 主要（MAJOR） | `plugins/chaogu/stock_utils.py` | 352 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 27 | Issue | 主要（MAJOR） | `plugins/chaogu/stock_utils.py` | 361 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 28 | Issue | 次要（MINOR） | `plugins/chaogu/stock_utils.py` | 518 | `python:S7498` | Replace this constructor call with a literal. | 构造器可替换为字面量，属于简化项。 |
| 29 | Issue | 次要（MINOR） | `plugins/chaogu/stock_utils.py` | 546 | `python:S7498` | Replace this constructor call with a literal. | 构造器可替换为字面量，属于简化项。 |
| 30 | Issue | 次要（MINOR） | `plugins/chaogu/stock_utils.py` | 547 | `python:S7498` | Replace this constructor call with a literal. | 构造器可替换为字面量，属于简化项。 |
| 31 | Issue | 主要（MAJOR） | `plugins/chaogu/stock_utils.py` | 630 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 32 | Issue | 主要（MAJOR） | `plugins/chaogu/stock_utils.py` | 744 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 33 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 525 | `python:S1192` | Define a constant instead of duplicating this literal "你还没有宠物！" 14 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 34 | Issue | 主要（MAJOR） | `plugins/chongwu/__init__.py` | 533 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 35 | Issue | 主要（MAJOR） | `plugins/chongwu/__init__.py` | 652 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 36 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 951 | `python:S1192` | Define a constant instead of duplicating this literal "最初的契约" 3 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 37 | Issue | 主要（MAJOR） | `plugins/chongwu/pet.py` | 1 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 38 | Issue | 严重（CRITICAL） | `plugins/chongwu/pet.py` | 154 | `python:S1192` | Define a constant instead of duplicating this literal 'SELECT items_data FROM user_items WHERE uid = ?' 3 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 39 | Issue | 次要（MINOR） | `plugins/chongwu/pet.py` | 251 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 40 | Issue | 次要（MINOR） | `plugins/chongwu/pet.py` | 290 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 41 | Issue | 主要（MAJOR） | `plugins/chongwu/petconfig.py` | 1 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 42 | Issue | 主要（MAJOR） | `plugins/english_guess/__init__.py` | 259 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 43 | Issue | 次要（MINOR） | `plugins/english_guess/__init__.py` | 340 | `python:S1481` | Remove the unused local variable "jpword". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 44 | Issue | 主要（MAJOR） | `plugins/english_guess/__init__.py` | 433 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 45 | Issue | 次要（MINOR） | `plugins/english_guess/__init__.py` | 480 | `python:S1481` | Remove the unused local variable "answer_str". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 46 | Issue | 次要（MINOR） | `plugins/english_guess/get_hint.py` | 24 | `python:S3626` | Remove this redundant continue. | 冗余 continue 可删除，行为通常不变。 |
| 47 | Issue | 主要（MAJOR） | `plugins/english_guess/guess_func.py` | 8 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 48 | Issue | 次要（MINOR） | `plugins/english_guess/guess_func.py` | 34 | `python:S1481` | Replace the unused loop index "i" with "_". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 49 | Issue | 主要（MAJOR） | `plugins/english_guess/guess_func.py` | 85 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 50 | Issue | 次要（MINOR） | `plugins/english_guess/guess_func.py` | 86 | `python:S3626` | Remove this redundant continue. | 冗余 continue 可删除，行为通常不变。 |
| 51 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 1 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 52 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 134 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 53 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 149 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 54 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 155 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 55 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 207 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 56 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 214 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 57 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 372 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 58 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 440 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 59 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 513 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 60 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 517 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 61 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 524 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 62 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 631 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 63 | Issue | 主要（MAJOR） | `plugins/feisheng/data.py` | 1 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 64 | Issue | 次要（MINOR） | `plugins/feisheng/data.py` | 58 | `python:S1481` | Remove the unused local variable "e". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 65 | Issue | 次要（MINOR） | `plugins/feisheng/data.py` | 187 | `python:S1481` | Remove the unused local variable "e". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 66 | Issue | 主要（MAJOR） | `plugins/fishing/__init__.py` | 689 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 67 | Issue | 主要（MAJOR） | `plugins/fishing/__init__.py` | 691 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 68 | Issue | 主要（MAJOR） | `plugins/fishing/__init__.py` | 760 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 69 | Issue | 主要（MAJOR） | `plugins/fishing/__init__.py` | 762 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 70 | Issue | 主要（MAJOR） | `plugins/fishing/getfish.py` | 1 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 71 | Issue | 主要（MAJOR） | `plugins/fishing/getfish.py` | 307 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 72 | Issue | 主要（MAJOR） | `plugins/fishing/getfish.py` | 321 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 73 | Issue | 次要（MINOR） | `plugins/fishing/getfish.py` | 348 | `python:S1481` | Remove the unused local variable "value_message". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 74 | Issue | 主要（MAJOR） | `plugins/fishing/getfish.py` | 370 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 75 | Issue | 主要（MAJOR） | `plugins/fishing/serif.py` | 1 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 76 | Issue | 主要（MAJOR） | `plugins/fishing/util.py` | 1 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |
| 77 | Issue | 主要（MAJOR） | `plugins/icelogin/__init__.py` | 173 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 78 | Issue | 严重（CRITICAL） | `plugins/icelogin/__init__.py` | 395 | `python:S1192` | Define a constant instead of duplicating this literal "不支持的平台类型" 3 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 79 | Issue | 次要（MINOR） | `plugins/icelogin/__init__.py` | 514 | `python:S1481` | Remove the unused local variable "platform_col". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 80 | Issue | 主要（MAJOR） | `plugins/icelogin/aslogin_v3.py` | 162 | `python:S1172` | Remove the unused function parameter "prefix". | 未使用参数可清理；若是框架/回调签名需保留。 |
| 81 | Issue | 主要（MAJOR） | `plugins/icelogin/aslogin_v3.py` | 216 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 82 | Issue | 主要（MAJOR） | `plugins/icelogin/aslogin_v3.py` | 224 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 83 | Issue | 主要（MAJOR） | `plugins/icelogin/aslogin_v3.py` | 289 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | 无插值 f-string 可改普通字符串，属于样式清理。 |
| 84 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 296 | `python:S1481` | Remove the unused local variable "is_bold". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 85 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 304 | `python:S117` | Rename this local variable "imageFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | 局部变量命名风格问题，低风险但收益偏整理。 |
| 86 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 305 | `python:S1192` | Define a constant instead of duplicating this literal 'HYShiGuangTiW_0.ttf' 6 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 87 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 351 | `python:S117` | Rename this local variable "iconFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | 局部变量命名风格问题，低风险但收益偏整理。 |
| 88 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 358 | `python:S1481` | Remove the unused local variable "e". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 89 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 375 | `python:S1192` | Define a constant instead of duplicating this literal 'yz.ttf' 12 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 90 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 377 | `python:S1481` | Replace the unused local variable "tip_w" with "_". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 91 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 377 | `python:S1481` | Replace the unused local variable "tip_h" with "_". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 92 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 446 | `python:S1481` | Replace the unused local variable "rp_h" with "_". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 93 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 449 | `python:S117` | Rename this local variable "infoImage" to match the regular expression ^[_a-z][a-z0-9_]*$. | 局部变量命名风格问题，低风险但收益偏整理。 |
| 94 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 451 | `python:S1481` | Replace the unused local variable "info_h" with "_". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 95 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 458 | `python:S117` | Rename this local variable "bonusIconFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | 局部变量命名风格问题，低风险但收益偏整理。 |
| 96 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 463 | `python:S117` | Rename this local variable "totalIconFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | 局部变量命名风格问题，低风险但收益偏整理。 |
| 97 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 471 | `python:S117` | Rename this local variable "loginFlagIconFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | 局部变量命名风格问题，低风险但收益偏整理。 |
| 98 | Issue | 主要（MAJOR） | `plugins/icelogin/aslogin_v3.py` | 512 | `python:S1172` | Remove the unused function parameter "guild_flag". | 未使用参数可清理；若是框架/回调签名需保留。 |
| 99 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 606 | `python:S117` | Rename this local variable "imageFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | 局部变量命名风格问题，低风险但收益偏整理。 |
| 100 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 620 | `python:S1481` | Replace the unused local variable "h" with "_". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 101 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 632 | `python:S117` | Rename this local variable "iconFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | 局部变量命名风格问题，低风险但收益偏整理。 |
| 102 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 639 | `python:S1481` | Remove the unused local variable "e". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 103 | Issue | 次要（MINOR） | `plugins/public_whitelist/__init__.py` | 503 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 104 | Issue | 次要（MINOR） | `plugins/public_whitelist/__init__.py` | 548 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 105 | Issue | 严重（CRITICAL） | `plugins/public_whitelist/__init__.py` | 732 | `python:S1192` | Define a constant instead of duplicating this literal "已结束领养云冰祈~" 5 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 106 | Issue | 次要（MINOR） | `plugins/shaojo/__init__.py` | 70 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 107 | Issue | 严重（CRITICAL） | `plugins/twenty_four/__init__.py` | 59 | `python:S1192` | Define a constant instead of duplicating this literal "本功能仅支持群组使用" 3 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 108 | Issue | 次要（MINOR） | `tools.py` | 49 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | async 无 await 可能是框架回调要求；逐处确认后再改。 |
| 109 | Issue | 主要（MAJOR） | `tools.py` | 131 | `python:S1066` | Merge this if statement with the enclosing one. | 合并嵌套 if 可读性更好，但通常不影响行为。 |
| 110 | Issue | 严重（CRITICAL） | `tools.py` | 244 | `python:S1192` | Define a constant instead of duplicating this literal 'base64://' 4 times. | 重复字面量可提常量；纯文案重复不一定值得立刻改。 |
| 111 | Issue | 次要（MINOR） | `tools.py` | 407 | `python:S1481` | Remove the unused local variable "name". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 112 | Issue | 次要（MINOR） | `tools.py` | 412 | `python:S1481` | Remove the unused local variable "name_height". | 未使用局部变量可删除或改为日志；通常是清理项。 |
| 113 | Issue | 主要（MAJOR） | `tools.py` | 421 | `python:S125` | Remove this commented out code. | 注释掉的代码建议清理，属于代码整洁项。 |

## 建议保留

共 101 条。

| # | 类型 | 严重程度 | 文件 | 行号 | 规则 | 问题 | 分档理由 |
|---:|---|---|---|---:|---|---|---|
| 1 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 498 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 2 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 499 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 3 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 504 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 4 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 523 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 5 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 641 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 6 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 986 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 7 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 1032 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 8 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 1033 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 9 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 1037 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 10 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 1039 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 11 | Security Hotspot | `中（MEDIUM）` | `plugins/chaogu/__init__.py` | 1047 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 12 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 178 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 13 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 191 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 14 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 199 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 15 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 200 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 16 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 207 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 17 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 218 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 18 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 662 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 19 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 663 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 20 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 754 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 21 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 762 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 22 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 766 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 23 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 770 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 24 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 774 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 25 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 778 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 26 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 779 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 27 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 787 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 28 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 825 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 29 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 830 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 30 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 845 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 31 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 886 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 32 | Security Hotspot | `中（MEDIUM）` | `plugins/chongwu/__init__.py` | 911 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 33 | Security Hotspot | `中（MEDIUM）` | `plugins/english_guess/__init__.py` | 285 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 34 | Security Hotspot | `中（MEDIUM）` | `plugins/english_guess/digit_guess_func.py` | 5 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 35 | Security Hotspot | `中（MEDIUM）` | `plugins/english_guess/guess_func.py` | 36 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 36 | Security Hotspot | `中（MEDIUM）` | `plugins/english_guess/guess_func.py` | 66 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 37 | Security Hotspot | `中（MEDIUM）` | `plugins/english_guess/guess_func.py` | 72 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 38 | Security Hotspot | `中（MEDIUM）` | `plugins/feisheng/__init__.py` | 143 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 39 | Security Hotspot | `中（MEDIUM）` | `plugins/feisheng/__init__.py` | 194 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 40 | Security Hotspot | `中（MEDIUM）` | `plugins/feisheng/__init__.py` | 358 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 41 | Security Hotspot | `中（MEDIUM）` | `plugins/feisheng/__init__.py` | 444 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 42 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/__init__.py` | 145 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 43 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 147 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 44 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 152 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 45 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 154 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 46 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 157 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 47 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 168 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 48 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 168 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 49 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 171 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 50 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 175 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 51 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 182 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 52 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 193 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 53 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 193 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 54 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 197 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 55 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 199 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 56 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 203 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 57 | Security Hotspot | `中（MEDIUM）` | `plugins/fishing/getfish.py` | 252 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 58 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 120 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 59 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 134 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 60 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 136 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 61 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 262 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 62 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 263 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 63 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 324 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 64 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 560 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 65 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 574 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 66 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 578 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 67 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 583 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 68 | Security Hotspot | `中（MEDIUM）` | `plugins/icelogin/aslogin_v3.py` | 596 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 69 | Security Hotspot | `中（MEDIUM）` | `plugins/twenty_four/__init__.py` | 72 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 70 | Security Hotspot | `中（MEDIUM）` | `utils.py` | 144 | `python:S2245` | Make sure that using this pseudorandom number generator is safe here. | 当前看起来是游戏、抽奖、签到、文案或展示用随机数，不是密钥/令牌；建议在 SonarQube 中标记为 reviewed/safe。 |
| 71 | Issue | 主要（MAJOR） | `build_image.py` | 122 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 72 | Issue | 主要（MAJOR） | `build_image.py` | 125 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 73 | Issue | 主要（MAJOR） | `build_image.py` | 131 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 74 | Issue | 主要（MAJOR） | `build_image.py` | 133 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 75 | Issue | 主要（MAJOR） | `build_image.py` | 387 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 76 | Issue | 主要（MAJOR） | `build_image.py` | 389 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 77 | Issue | 主要（MAJOR） | `build_image.py` | 405 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 78 | Issue | 主要（MAJOR） | `build_image.py` | 407 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 79 | Issue | 主要（MAJOR） | `build_image.py` | 411 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 80 | Issue | 主要（MAJOR） | `build_image.py` | 451 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 81 | Issue | 主要（MAJOR） | `build_image.py` | 453 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 82 | Issue | 主要（MAJOR） | `build_image.py` | 457 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 83 | Issue | 主要（MAJOR） | `build_image.py` | 497 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 84 | Issue | 主要（MAJOR） | `build_image.py` | 523 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 85 | Issue | 主要（MAJOR） | `build_image.py` | 532 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 86 | Issue | 主要（MAJOR） | `build_image.py` | 727 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 87 | Issue | 主要（MAJOR） | `build_image.py` | 743 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 88 | Issue | 主要（MAJOR） | `build_image.py` | 894 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 89 | Issue | 主要（MAJOR） | `build_image.py` | 912 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 90 | Issue | 主要（MAJOR） | `money.py` | 157 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 91 | Issue | 主要（MAJOR） | `money.py` | 421 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 92 | Issue | 主要（MAJOR） | `money.py` | 475 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 93 | Issue | 主要（MAJOR） | `resources.py` | 27 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 94 | Issue | 主要（MAJOR） | `resources.py` | 63 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 95 | Issue | 主要（MAJOR） | `resources.py` | 124 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 96 | Issue | 主要（MAJOR） | `resources.py` | 170 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 97 | Issue | 主要（MAJOR） | `tools.py` | 555 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 98 | Issue | 主要（MAJOR） | `utils.py` | 21 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 99 | Issue | 主要（MAJOR） | `utils.py` | 36 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 100 | Issue | 主要（MAJOR） | `utils.py` | 73 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |
| 101 | Issue | 主要（MAJOR） | `utils.py` | 119 | `python:S6546` | Use a union type expression for this type hint. | 仅是 Python 3.10+ 联合类型语法偏好；未确认运行版本前不建议批量改。 |

