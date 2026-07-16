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
| 5 | Issue | 严重（CRITICAL） | `build_image.py` | 116 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 61 to the 15 allowed. | ✅ 已修复并验证：构造流程拆为选项解析、画布创建、背景加载、透明化和初始文本辅助函数；校准复杂度 5，兼容性/图像行为测试、全量 unittest 与 compileall 通过。 |
| 6 | Issue | 严重（CRITICAL） | `build_image.py` | 212 | `python:S5754` | Specify an exception class to catch or reraise the exception | ✅ 已修复并验证：限定捕获 `TypeError`；AST 回归测试、全量 unittest 与 compileall 通过。 |
| 7 | Issue | 严重（CRITICAL） | `build_image.py` | 234 | `python:S5797` | Replace this expression; used as a condition it will always be constant. | ✅ 已修复并验证：改为真实 `Union["BuildImage", Image.Image]` 注解；AST 回归测试通过。 |
| 8 | Issue | 严重（CRITICAL） | `build_image.py` | 250 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | ✅ 已修复并验证：居中定位与透明粘贴拆分；校准复杂度 4，图像行为回归测试、全量 unittest 与 compileall 通过。 |
| 9 | Issue | 严重（CRITICAL） | `build_image.py` | 252 | `python:S5797` | Replace this expression; used as a condition it will always be constant. | ✅ 已修复并验证：改为真实 `Union["BuildImage", Image.Image]` 注解；AST 回归测试通过。 |
| 10 | Issue | 主要（MAJOR） | `build_image.py` | 571 | `python:S112` | Replace this generic exception class with a more specific one. | ✅ 已修复并验证：缺少尺寸参数时改抛 `ValueError`；AST 回归测试、全量 unittest 与 compileall 通过。 |
| 11 | Issue | 严重（CRITICAL） | `build_image.py` | 910 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 19 to the 15 allowed. | ✅ 已修复并验证：颜色范围解析与匹配逻辑拆分；校准复杂度 6，并新增精确/范围替色行为测试通过。 |
| 12 | Issue | 严重（CRITICAL） | `plugins/ai_draw/__init__.py` | 267 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 36 to the 15 allowed. | ✅ 已修复并验证：按适配器拆分 URL 提取并独立下载；校准复杂度 1，AI 图片响应测试与 compileall 通过。 |
| 13 | Issue | 严重（CRITICAL） | `plugins/ai_draw/_image_response.py` | 47 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed. | ✅ 已修复并验证：数据项校验和响应字段优先级拆分；校准复杂度 6，13 个图片响应行为测试通过。 |
| 14 | Issue | 严重（CRITICAL） | `plugins/call_me_please/__init__.py` | 54 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 21 to the 15 allowed. | ✅ 已修复并验证：图片拒绝消息、显示长度计算和屏蔽词判断拆分；校准复杂度 8，全量 unittest 与 compileall 通过。 |
| 15 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 177 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 19 to the 15 allowed. | ✅ 已修复并验证：图表生成和文字回退拆分；校准复杂度 9，compileall 与全量 unittest 通过。 |
| 16 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 433 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | ✅ 已修复并验证：事件收集和单条格式化拆分；校准复杂度 1，辅助函数最高复杂度 4。 |
| 17 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 474 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 24 to the 15 allowed. | ✅ 已修复并验证：事件触发、价格边界和普通波动拆分；校准复杂度 5，辅助函数均低于 15，compileall 通过。 |
| 18 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 492 | `python:S5754` | Specify an exception class to catch or reraise the exception | ✅ 已修复并验证：限定捕获数据形态相关异常；AST 回归测试、全量 unittest 与 compileall 通过。 |
| 19 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 1193 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 19 to the 15 allowed. | ✅ 已修复并验证：at 目标、金额和 QQ 回退解析拆分；校准复杂度 6，异常回归测试与 compileall 通过。 |
| 20 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 157 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 33 to the 15 allowed. | ✅ 已修复并验证：已有宠物处理、奖池选择和空扭蛋奖励拆分；校准复杂度 6，compileall 与全量 unittest 通过。 |
| 21 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 716 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 29 to the 15 allowed. | ✅ 已修复并验证：事件日期解析和单技能效果拆分；校准复杂度 10，技能辅助函数复杂度 10。 |
| 22 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 814 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 22 to the 15 allowed. | ✅ 已修复并验证：进化条件和下一形态选择拆分；校准复杂度 8，compileall 通过。 |
| 23 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 866 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 20 to the 15 allowed. | ✅ 已修复并验证：原始进化路线查找拆分；校准复杂度 8，compileall 通过。 |
| 24 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 1053 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 24 to the 15 allowed. | ✅ 已修复并验证：可排行宠物收集、飞升标记和排序统一抽取；校准复杂度 7。 |
| 25 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 1118 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 31 to the 15 allowed. | ✅ 已修复并验证：复用排行条目并独立计算并列排名；校准复杂度 8，compileall 与全量 unittest 通过。 |
| 26 | Issue | 严重（CRITICAL） | `plugins/english_guess/__init__.py` | 132 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 19 to the 15 allowed. | ✅ 已修复并验证：Wordle 参数解析拆为纯函数；校准复杂度 2，参数顺序行为测试通过。 |
| 27 | Issue | 严重（CRITICAL） | `plugins/english_guess/__init__.py` | 398 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | ✅ 已修复并验证：过期处理、匹配状态、绘制和轮次收尾拆分；校准复杂度 5，匹配逻辑测试通过。 |
| 28 | Issue | 主要（MAJOR） | `plugins/english_guess/__init__.py` | 401 | `python:S5869` | Remove duplicates in this character class. | ✅ 已修复并验证：改用 `re.fullmatch(r"[A-Za-z]+", ...)`；AST 回归测试通过。 |
| 29 | Issue | 严重（CRITICAL） | `plugins/english_guess/__init__.py` | 477 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 28 to the 15 allowed. | ✅ 已修复并验证：数字匹配、绘制和通用轮次收尾拆分；校准复杂度 4，重复数字匹配测试通过。 |
| 30 | Issue | 严重（CRITICAL） | `plugins/english_guess/__init__.py` | 560 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed. | ✅ 已修复并验证：日语假名绘制与通用轮次收尾拆分；校准复杂度 4，compileall 与全量 unittest 通过。 |
| 31 | Issue | 严重（CRITICAL） | `plugins/english_guess/get_hint.py` | 5 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 31 to the 15 allowed. | ✅ 已修复并验证：改为分阶段推导式过滤并安全关闭文件；校准复杂度 2，错误字母/精确位置行为测试通过。 |
| 32 | Issue | 严重（CRITICAL） | `plugins/english_guess/guess_func.py` | 30 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed. | ✅ 已修复并验证：单轮匹配提取为 `_apply_guess`，并修正成功长度不再硬编码 5；校准复杂度 5，7 字母行为测试通过。 |
| 33 | Issue | 严重（CRITICAL） | `plugins/feisheng/__init__.py` | 264 | `python:S5754` | Specify an exception class to catch or reraise the exception | ✅ 已修复并验证：数量转换仅捕获 `ValueError`；AST 回归测试、全量 unittest 与 compileall 通过。 |
| 34 | Issue | 严重（CRITICAL） | `plugins/feisheng/__init__.py` | 394 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 20 to the 15 allowed. | ✅ 已修复并验证：确认提示、渡劫判定和剧情生成拆分为独立函数；校准复杂度由 20 降至 10，三类结果测试与编译通过。 |
| 35 | Issue | 严重（CRITICAL） | `plugins/feisheng/__init__.py` | 484 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 18 to the 15 allowed. | ✅ 已修复并验证：进度展示和下一步提示拆分为纯函数；校准复杂度由 18 降至 3，四种状态测试与编译通过。 |
| 36 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 625 | `python:S3923` | Remove this if statement or edit its code blocks so that they're not all the same. | ✅ 已修复并验证：移除行为完全相同的内层排名分支；AST 回归测试与全量 unittest 通过。 |
| 37 | Issue | 严重（CRITICAL） | `plugins/fishing/getfish.py` | 126 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 34 to the 15 allowed. | ✅ 已修复并验证：鱼种选择、鱼获和金币结果拆分，概率区间改为清晰的累计边界；校准复杂度降至 8，边界测试与编译通过。 |
| 38 | Issue | 严重（CRITICAL） | `plugins/fishing/getfish.py` | 221 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 55 to the 15 allowed. | ✅ 已修复并验证：资源检查、限额、扣费、汇总、奖励和发送拆分；校准复杂度降至 1，奖励/消息测试与编译通过。 |
| 39 | Issue | 严重（CRITICAL） | `plugins/fishing/util.py` | 108 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 21 to the 15 allowed. | ✅ 已修复并验证：每日限额的插入/更新决策抽为纯函数；校准复杂度降至 3，新增、更新、跨日及超限测试与编译通过。 |
| 40 | Issue | 严重（CRITICAL） | `plugins/hongbao/__init__.py` | 87 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | ✅ 已修复并验证：参数解析抽离，并移除已由 `get_session` 处理的不可达过期分支；校准复杂度降至 10，解析测试与编译通过。 |
| 41 | Issue | 严重（CRITICAL） | `plugins/icelogin/__init__.py` | 203 | `python:S5754` | Specify an exception class to catch or reraise the exception | ✅ 已修复并验证：限定捕获消息结构相关异常；AST 回归测试、全量 unittest 与 compileall 通过。 |
| 42 | Issue | 主要（MAJOR） | `plugins/icelogin/__init__.py` | 329 | `python:S1871` | Either merge this branch with the identical one on line "327" or change one of the implementations. | ✅ 已修复并验证：合并两个私聊事件判断后统一赋值；AST 回归测试通过。 |
| 43 | Issue | 严重（CRITICAL） | `plugins/icelogin/__init__.py` | 577 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 34 to the 15 allowed. | ✅ 已修复并验证：适配器图片地址提取、下载、居中裁剪与保存拆分；校准复杂度由 34 降至 2，来源和裁剪行为测试与编译通过。 |
| 44 | Issue | 主要（MAJOR） | `plugins/icelogin/__init__.py` | 604 | `python:S1871` | Either merge this branch with the identical one on line "600" or change one of the implementations. | ✅ 已修复并验证：统一按附件 URL 提取，删除相同赋值分支；AST 回归测试通过。 |
| 45 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 114 | `python:S5754` | Specify an exception class to catch or reraise the exception | ✅ 已修复并验证：头像下载仅捕获 aiohttp/超时异常；AST 回归测试与 compileall 通过。 |
| 46 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 170 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 99 to the 15 allowed. | ✅ 已修复并验证：签到奖励状态、背景、头像、身份、运势和奖励绘制分层拆分；主函数校准复杂度由 99 降至 1，辅助函数均不超过 11，规则测试与编译通过。 |
| 47 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 313 | `python:S5754` | Specify an exception class to catch or reraise the exception | ✅ 已修复并验证：自定义背景处理限定捕获图像/类型异常；AST 回归测试与 compileall 通过。 |
| 48 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 512 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 39 to the 15 allowed. | ✅ 已修复并验证：资产背景规则、头像复用和钱包文字绘制拆分；主函数校准复杂度由 39 降至 1，背景解锁规则测试与编译通过。 |
| 49 | Issue | 严重（CRITICAL） | `plugins/public_whitelist/__init__.py` | 511 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed. | ✅ 已修复并验证：表单校验、白名单命中和审核状态渲染抽为同步决策函数；Web 处理器复杂度降至 0，决策函数复杂度 10，状态测试与编译通过。 |
| 50 | Issue | 严重（CRITICAL） | `plugins/shaojo/__init__.py` | 88 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | ✅ 已修复并验证：消息段解析、原始 CQ at 补充和 UID 去重拆分；校准复杂度降至 1，双适配器映射与去重测试通过。 |
| 51 | Issue | 严重（CRITICAL） | `plugins/shaojo/choicer.py` | 28 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 18 to the 15 allowed. | ✅ 已修复并验证：列表选择编译和映射配置编译拆分；校准复杂度降至 3，既有稳定生成测试通过。 |
| 52 | Issue | 严重（CRITICAL） | `plugins/shaojo/choicer.py` | 84 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 17 to the 15 allowed. | ✅ 已修复并验证：重复模板与权重选择执行拆分；校准复杂度降至 4，既有稳定生成测试通过。 |
| 53 | Issue | 严重（CRITICAL） | `tools.py` | 145 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 16 to the 15 allowed. | ✅ 已修复并验证：QQBot 头像的 AppID、绑定 QQ 和事件头像回退抽为辅助函数；校准复杂度由 16 降至 2，编译通过。 |
| 54 | Issue | 严重（CRITICAL） | `tools.py` | 177 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 70 to the 15 allowed. | ✅ 已修复并验证：节点规范化、消息段转换、图片转换和逐条降级发送拆分；校准复杂度由 70 降至 3，Base64/URL 转换测试与编译通过。 |
| 55 | Issue | 严重（CRITICAL） | `tools.py` | 404 | `python:S3776` | Refactor this function to reduce its Cognitive Complexity from 88 to the 15 allowed. | ✅ 已修复并验证：文本测量换行、图片下载/缩放和单段绘制拆分；校准复杂度由 88 降至 3，换行行为测试与编译通过。 |

## 可选修复

共 113 条。

| # | 类型 | 严重程度 | 文件 | 行号 | 规则 | 问题 | 分档理由 |
|---:|---|---|---|---:|---|---|---|
| 1 | Issue | 主要（MAJOR） | `build_image.py` | 14 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：删除未启用且依赖已不存在库的图像哈希比较代码块，并移除对应未使用导入；源码测试与编译通过。 |
| 2 | Issue | 主要（MAJOR） | `build_image.py` | 117 | `python:S107` | Method "__init__" has 16 parameters, which is greater than the 13 authorized. | ✅ 已修复并验证：选项归入兼容 `*args/**kwargs` 解析层，显式参数数降至规则阈值内；旧位置参数与现有关键字参数兼容性测试通过。 |
| 3 | Issue | 次要（MINOR） | `build_image.py` | 184 | `python:S116` | Rename this field "markImg" to match the regular expression ^[_a-z][_a-z0-9]*$. | ✅ 已修复并验证：内部字段改为 `mark_img`，并以动态别名保留旧 `markImg` 读写兼容；AST 不再存在 camelCase 属性，兼容行为测试通过。 |
| 4 | Issue | 严重（CRITICAL） | `build_image.py` | 269 | `python:S1192` | Define a constant instead of duplicating this literal "center_type must be 'center', 'by_width' or 'by_height'" 3 times. | ✅ 已修复并验证：三处统一复用 `_CENTER_TYPE_ERROR`；原字面量仅保留常量定义一处，源码测试通过。 |
| 5 | Issue | 主要（MAJOR） | `build_image.py` | 499 | `python:S1172` | Remove the unused function parameter "center_type". | ✅ 已修复并验证：`get_multi_size` 删除未使用参数，仓库内无调用点需要迁移；签名 AST 测试与编译通过。 |
| 6 | Issue | 次要（MINOR） | `build_image.py` | 892 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已修复并验证：`areplace_color_tran` 现在等待线程池任务完成；异步替色行为测试与编译通过。 |
| 7 | Issue | 次要（MINOR） | `money.py` | 35 | `python:S7508` | Remove this redundant call. | ✅ 已核对并验证：此项指 `list(DEFAULT_ASSETS.keys())` 中冗余的 `.keys()`，已改为 `list(DEFAULT_ASSETS)`；从调用栈获取 UID 的 `_find_uid_in_stack()` 完整保留，并增加 AST 回归保护。 |
| 8 | Issue | 次要（MINOR） | `plugins/ai_draw/_image_response.py` | 87 | `python:S5713` | Remove this redundant Exception class; it derives from another which is already caught. | ✅ 已修复并验证：仅捕获父类 `ValueError`；既有无效 Base64 行为测试及 AST 回归测试通过。 |
| 9 | Issue | 主要（MAJOR） | `plugins/call_me_please/__init__.py` | 82 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描与 compileall 通过。 |
| 10 | Issue | 主要（MAJOR） | `plugins/call_me_please/__init__.py` | 91 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描与 compileall 通过。 |
| 11 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 192 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 12 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 202 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 13 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 212 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 14 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 224 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 15 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 629 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已修复并验证：赌博轮次计算改为同步函数并更新两个调用点；AST 扫描与 compileall 通过。 |
| 16 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 784 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 17 | Issue | 主要（MAJOR） | `plugins/chaogu/__init__.py` | 836 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 18 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 989 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已修复并验证：钱包翻倍处理器改为同步，统一分发器兼容同步/异步结果；AST 扫描与 compileall 通过。 |
| 19 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 996 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已修复并验证：钱包扣减处理器改为同步，统一分发器兼容同步/异步结果；AST 扫描与 compileall 通过。 |
| 20 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 1018 | `python:S7519` | Replace with dict fromkeys method call | ✅ 已修复并验证：改用 `dict.fromkeys`；AST/源码扫描与 compileall 通过。 |
| 21 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 1044 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已修复并验证：钓鱼次数奖励改为同步函数并更新调用点；AST 扫描与 compileall 通过。 |
| 22 | Issue | 严重（CRITICAL） | `plugins/chaogu/__init__.py` | 1181 | `python:S1192` | Define a constant instead of duplicating this literal "金额必须是数字！" 5 times. | ✅ 已修复并验证：提取 `AMOUNT_NUMBER_ERROR` 常量并替换全部重复用法；字面量扫描通过。 |
| 23 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 1199 | `python:S5713` | Remove this redundant Exception class; it derives from another which is already caught. | ✅ 已修复并验证：目标解析仅捕获实际会抛出的 `ValueError`；AST 回归测试通过。 |
| 24 | Issue | 次要（MINOR） | `plugins/chaogu/__init__.py` | 1199 | `python:S5713` | Remove this redundant Exception class; it derives from another which is already caught. | ✅ 已修复并验证：冗余父/子异常组合已移除；AST 回归测试通过。 |
| 25 | Issue | 主要（MAJOR） | `plugins/chaogu/stock_utils.py` | 1 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：移除被识别为注释代码的文件头字符串；源码扫描与 compileall 通过。 |
| 26 | Issue | 主要（MAJOR） | `plugins/chaogu/stock_utils.py` | 352 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 27 | Issue | 主要（MAJOR） | `plugins/chaogu/stock_utils.py` | 361 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 28 | Issue | 次要（MINOR） | `plugins/chaogu/stock_utils.py` | 518 | `python:S7498` | Replace this constructor call with a literal. | ✅ 已修复并验证：`arrowprops` 改为字典字面量；源码扫描与 compileall 通过。 |
| 29 | Issue | 次要（MINOR） | `plugins/chaogu/stock_utils.py` | 546 | `python:S7498` | Replace this constructor call with a literal. | ✅ 已修复并验证：`arrowprops` 改为字典字面量；源码扫描与 compileall 通过。 |
| 30 | Issue | 次要（MINOR） | `plugins/chaogu/stock_utils.py` | 547 | `python:S7498` | Replace this constructor call with a literal. | ✅ 已修复并验证：`bbox` 改为字典字面量；源码扫描与 compileall 通过。 |
| 31 | Issue | 主要（MAJOR） | `plugins/chaogu/stock_utils.py` | 630 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：移除被识别为注释代码的函数字符串；源码扫描与 compileall 通过。 |
| 32 | Issue | 主要（MAJOR） | `plugins/chaogu/stock_utils.py` | 744 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：移除被识别为注释代码的函数字符串；源码扫描与 compileall 通过。 |
| 33 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 525 | `python:S1192` | Define a constant instead of duplicating this literal "你还没有宠物！" 14 times. | ✅ 已修复并验证：提取 `NO_PET_MESSAGE` 并替换所有完全重复用法；字面量扫描通过。 |
| 34 | Issue | 主要（MAJOR） | `plugins/chongwu/__init__.py` | 533 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 35 | Issue | 主要（MAJOR） | `plugins/chongwu/__init__.py` | 652 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 36 | Issue | 严重（CRITICAL） | `plugins/chongwu/__init__.py` | 951 | `python:S1192` | Define a constant instead of duplicating this literal "最初的契约" 3 times. | ✅ 已修复并验证：提取 `ORIGINAL_CONTRACT_ITEM`，帮助文本和提示均复用；字面量扫描通过。 |
| 37 | Issue | 主要（MAJOR） | `plugins/chongwu/pet.py` | 1 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：移除被识别为注释代码的文件头字符串；源码扫描与 compileall 通过。 |
| 38 | Issue | 严重（CRITICAL） | `plugins/chongwu/pet.py` | 154 | `python:S1192` | Define a constant instead of duplicating this literal 'SELECT items_data FROM user_items WHERE uid = ?' 3 times. | ✅ 已修复并验证：提取 `USER_ITEMS_QUERY` 并替换 3 处查询；字面量扫描通过。 |
| 39 | Issue | 次要（MINOR） | `plugins/chongwu/pet.py` | 251 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已修复并验证：状态更新改为同步函数并更新全部 16 个调用点；AST 扫描与 compileall 通过。 |
| 40 | Issue | 次要（MINOR） | `plugins/chongwu/pet.py` | 290 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已修复并验证：进化检查改为同步函数；AST 扫描与 compileall 通过。 |
| 41 | Issue | 主要（MAJOR） | `plugins/chongwu/petconfig.py` | 1 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：移除被识别为注释代码的文件头字符串；源码扫描与 compileall 通过。 |
| 42 | Issue | 主要（MAJOR） | `plugins/english_guess/__init__.py` | 259 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 43 | Issue | 次要（MINOR） | `plugins/english_guess/__init__.py` | 340 | `python:S1481` | Remove the unused local variable "jpword". | ✅ 已修复并验证：删除退出日语游戏分支中的未使用变量；AST/源码扫描通过。 |
| 44 | Issue | 主要（MAJOR） | `plugins/english_guess/__init__.py` | 433 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 45 | Issue | 次要（MINOR） | `plugins/english_guess/__init__.py` | 480 | `python:S1481` | Remove the unused local variable "answer_str". | ✅ 已修复并验证：删除未使用的答案字符串；AST/源码扫描通过。 |
| 46 | Issue | 次要（MINOR） | `plugins/english_guess/get_hint.py` | 24 | `python:S3626` | Remove this redundant continue. | ✅ 已修复并验证：过滤逻辑改写后冗余 `continue` 消除；行为单元测试通过。 |
| 47 | Issue | 主要（MAJOR） | `plugins/english_guess/guess_func.py` | 8 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：路径改为普通字符串；无插值 f-string 扫描通过。 |
| 48 | Issue | 次要（MINOR） | `plugins/english_guess/guess_func.py` | 34 | `python:S1481` | Replace the unused loop index "i" with "_". | ✅ 已修复并验证：未使用索引改为 `_`；AST/源码扫描通过。 |
| 49 | Issue | 主要（MAJOR） | `plugins/english_guess/guess_func.py` | 85 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：改为普通字符串；无插值 f-string 扫描通过。 |
| 50 | Issue | 次要（MINOR） | `plugins/english_guess/guess_func.py` | 86 | `python:S3626` | Remove this redundant continue. | ✅ 已修复并验证：输入循环改为成功即返回，冗余 `continue/else` 消除；compileall 通过。 |
| 51 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 1 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：移除文件首部被识别为注释代码的字符串块；AST 清理测试与编译通过。 |
| 52 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 134 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；全文件 AST 无冗余 f-string，编译通过。 |
| 53 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 149 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；全文件 AST 无冗余 f-string，编译通过。 |
| 54 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 155 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；全文件 AST 无冗余 f-string，编译通过。 |
| 55 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 207 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；全文件 AST 无冗余 f-string，编译通过。 |
| 56 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 214 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；全文件 AST 无冗余 f-string，编译通过。 |
| 57 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 372 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；全文件 AST 无冗余 f-string，编译通过。 |
| 58 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 440 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；渡劫成功、消耗失败测试与编译通过。 |
| 59 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 513 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；全文件 AST 无冗余 f-string，编译通过。 |
| 60 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 517 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；进度状态测试与编译通过。 |
| 61 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 524 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；进度状态测试与编译通过。 |
| 62 | Issue | 主要（MAJOR） | `plugins/feisheng/__init__.py` | 631 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：无插值 f-string 改为普通字符串；全文件 AST 无冗余 f-string，编译通过。 |
| 63 | Issue | 主要（MAJOR） | `plugins/feisheng/data.py` | 1 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：移除文件首部被识别为注释代码的字符串块；AST 清理测试与编译通过。 |
| 64 | Issue | 次要（MINOR） | `plugins/feisheng/data.py` | 58 | `python:S1481` | Remove the unused local variable "e". | ✅ 已修复并验证：异常处理不再绑定未使用变量；AST 异常变量检查与编译通过。 |
| 65 | Issue | 次要（MINOR） | `plugins/feisheng/data.py` | 187 | `python:S1481` | Remove the unused local variable "e". | ✅ 已修复并验证：异常处理不再绑定未使用变量；AST 异常变量检查与编译通过。 |
| 66 | Issue | 主要（MAJOR） | `plugins/fishing/__init__.py` | 689 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：分隔线无插值 f-string 改为普通字符串；AST 清理测试与编译通过。 |
| 67 | Issue | 主要（MAJOR） | `plugins/fishing/__init__.py` | 691 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：分隔线无插值 f-string 改为普通字符串；AST 清理测试与编译通过。 |
| 68 | Issue | 主要（MAJOR） | `plugins/fishing/__init__.py` | 760 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：分隔线无插值 f-string 改为普通字符串；AST 清理测试与编译通过。 |
| 69 | Issue | 主要（MAJOR） | `plugins/fishing/__init__.py` | 762 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：分隔线无插值 f-string 改为普通字符串；AST 清理测试与编译通过。 |
| 70 | Issue | 主要（MAJOR） | `plugins/fishing/getfish.py` | 1 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：移除文件首部被识别为注释代码的字符串块；AST 清理测试与编译通过。 |
| 71 | Issue | 主要（MAJOR） | `plugins/fishing/getfish.py` | 307 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：固定提示改为普通字符串并纳入消息构建函数；AST 清理测试与消息测试通过。 |
| 72 | Issue | 主要（MAJOR） | `plugins/fishing/getfish.py` | 321 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：固定补贴提示由统一消息构建函数生成；AST 清理测试与补贴消息测试通过。 |
| 73 | Issue | 次要（MINOR） | `plugins/fishing/getfish.py` | 348 | `python:S1481` | Remove the unused local variable "value_message". | ✅ 已修复并验证：删除整段未使用的价值消息构建；AST 不再存在该赋值，编译通过。 |
| 74 | Issue | 主要（MAJOR） | `plugins/fishing/getfish.py` | 370 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：删除废弃的合并转发与单独发送注释代码；源码回归检查与编译通过。 |
| 75 | Issue | 主要（MAJOR） | `plugins/fishing/serif.py` | 1 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：移除文件首部被识别为注释代码的字符串块；AST 清理测试与编译通过。 |
| 76 | Issue | 主要（MAJOR） | `plugins/fishing/util.py` | 1 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：移除文件首部被识别为注释代码的字符串块；AST 清理测试与编译通过。 |
| 77 | Issue | 主要（MAJOR） | `plugins/icelogin/__init__.py` | 173 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：固定昵称提示改为普通字符串；全文件 AST 无冗余 f-string，编译通过。 |
| 78 | Issue | 严重（CRITICAL） | `plugins/icelogin/__init__.py` | 395 | `python:S1192` | Define a constant instead of duplicating this literal "不支持的平台类型" 3 times. | ✅ 已修复并验证：提取 `UNSUPPORTED_PLATFORM_MESSAGE` 并复用三处；字面量计数测试与编译通过。 |
| 79 | Issue | 次要（MINOR） | `plugins/icelogin/__init__.py` | 514 | `python:S1481` | Remove the unused local variable "platform_col". | ✅ 已修复并验证：解绑预确认仅校验适配器，不再创建未使用的平台列变量；AST 回归测试与编译通过。 |
| 80 | Issue | 主要（MAJOR） | `plugins/icelogin/aslogin_v3.py` | 162 | `python:S1172` | Remove the unused function parameter "prefix". | ✅ 已修复并验证：`save_to_local` 删除未使用参数并更新两处调用；签名 AST 测试与编译通过。 |
| 81 | Issue | 主要（MAJOR） | `plugins/icelogin/aslogin_v3.py` | 216 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：生日固定奖励提示改为普通字符串；全文件 AST 无冗余 f-string。 |
| 82 | Issue | 主要（MAJOR） | `plugins/icelogin/aslogin_v3.py` | 224 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：节日固定奖励提示改为普通字符串；全文件 AST 无冗余 f-string。 |
| 83 | Issue | 主要（MAJOR） | `plugins/icelogin/aslogin_v3.py` | 289 | `python:S3457` | Add replacement fields or use a normal string instead of an f-string. | ✅ 已修复并验证：匿名钱包固定文本改为普通字符串；全文件 AST 无冗余 f-string。 |
| 84 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 296 | `python:S1481` | Remove the unused local variable "is_bold". | ✅ 已修复并验证：删除未使用的粗体标志，边框状态直接由背景构建结果返回；AST 清理测试通过。 |
| 85 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 304 | `python:S117` | Rename this local variable "imageFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | ✅ 已修复并验证：背景路径统一使用 `image_file` 等 snake_case 名称；AST 清理测试与编译通过。 |
| 86 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 305 | `python:S1192` | Define a constant instead of duplicating this literal 'HYShiGuangTiW_0.ttf' 6 times. | ✅ 已修复并验证：提取 `SIGN_FONT` 常量；原字面量仅保留定义一处，计数测试通过。 |
| 87 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 351 | `python:S117` | Rename this local variable "iconFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | ✅ 已修复并验证：远程头像字节流由共享头像函数直接处理，不再存在 camelCase 变量；AST 清理测试通过。 |
| 88 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 358 | `python:S1481` | Remove the unused local variable "e". | ✅ 已修复并验证：头像失败降级不再绑定未使用异常变量；全文件异常变量 AST 检查通过。 |
| 89 | Issue | 严重（CRITICAL） | `plugins/icelogin/aslogin_v3.py` | 375 | `python:S1192` | Define a constant instead of duplicating this literal 'yz.ttf' 12 times. | ✅ 已修复并验证：提取 `BODY_FONT` 常量；原字面量仅保留定义一处，计数测试通过。 |
| 90 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 377 | `python:S1481` | Replace the unused local variable "tip_w" with "_". | ✅ 已修复并验证：默认头像提示不再读取未使用的尺寸；AST 清理测试通过。 |
| 91 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 377 | `python:S1481` | Replace the unused local variable "tip_h" with "_". | ✅ 已修复并验证：默认头像提示不再读取未使用的尺寸；AST 清理测试通过。 |
| 92 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 446 | `python:S1481` | Replace the unused local variable "rp_h" with "_". | ✅ 已修复并验证：运势数字尺寸仅解包实际使用的宽度；AST 清理测试通过。 |
| 93 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 449 | `python:S117` | Rename this local variable "infoImage" to match the regular expression ^[_a-z][a-z0-9_]*$. | ✅ 已修复并验证：变量改为 `info_image`；AST 命名清理测试与编译通过。 |
| 94 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 451 | `python:S1481` | Replace the unused local variable "info_h" with "_". | ✅ 已修复并验证：评语尺寸仅解包实际使用的宽度；AST 清理测试通过。 |
| 95 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 458 | `python:S117` | Rename this local variable "bonusIconFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | ✅ 已修复并验证：变量改为 `bonus_icon_file`；AST 命名清理测试与编译通过。 |
| 96 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 463 | `python:S117` | Rename this local variable "totalIconFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | ✅ 已修复并验证：变量改为 `total_icon_file`；AST 命名清理测试与编译通过。 |
| 97 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 471 | `python:S117` | Rename this local variable "loginFlagIconFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | ✅ 已修复并验证：变量改为 `login_flag_icon_file`；AST 命名清理测试与编译通过。 |
| 98 | Issue | 主要（MAJOR） | `plugins/icelogin/aslogin_v3.py` | 512 | `python:S1172` | Remove the unused function parameter "guild_flag". | ✅ 已修复并验证：`get_purse` 删除未使用参数，唯一调用点无需兼容调整；签名 AST 测试与编译通过。 |
| 99 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 606 | `python:S117` | Rename this local variable "imageFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | ✅ 已修复并验证：钱包背景路径改为 `image_file`；AST 命名清理测试与编译通过。 |
| 100 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 620 | `python:S1481` | Replace the unused local variable "h" with "_". | ✅ 已修复并验证：共享头像函数仅解包实际使用的宽度；AST 清理测试通过。 |
| 101 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 632 | `python:S117` | Rename this local variable "iconFile" to match the regular expression ^[_a-z][a-z0-9_]*$. | ✅ 已修复并验证：钱包远程头像复用共享字节流处理，不再存在 camelCase 变量；AST 清理测试通过。 |
| 102 | Issue | 次要（MINOR） | `plugins/icelogin/aslogin_v3.py` | 639 | `python:S1481` | Remove the unused local variable "e". | ✅ 已修复并验证：钱包头像失败降级不再绑定未使用异常变量；全文件异常变量 AST 检查通过。 |
| 103 | Issue | 次要（MINOR） | `plugins/public_whitelist/__init__.py` | 503 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已核对并验证：该函数是直接注册给 aiohttp 的异步请求处理器，必须保持 async；添加带理由的 `NOSONAR` 抑制误报，并用 AST 验证注册关系。 |
| 104 | Issue | 次要（MINOR） | `plugins/public_whitelist/__init__.py` | 548 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已核对并验证：健康检查是直接注册给 aiohttp 的异步请求处理器，必须保持 async；添加带理由的 `NOSONAR` 抑制误报，并用 AST 验证注册关系。 |
| 105 | Issue | 严重（CRITICAL） | `plugins/public_whitelist/__init__.py` | 732 | `python:S1192` | Define a constant instead of duplicating this literal "已结束领养云冰祈~" 5 times. | ✅ 已修复并验证：提取 `ADOPTION_ENDED_MESSAGE` 并替换五处；字面量计数测试与编译通过。 |
| 106 | Issue | 次要（MINOR） | `plugins/shaojo/__init__.py` | 70 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已修复并验证：Rule 检查函数改为同步函数，保持相同布尔判断；AST 签名测试与编译通过。 |
| 107 | Issue | 严重（CRITICAL） | `plugins/twenty_four/__init__.py` | 59 | `python:S1192` | Define a constant instead of duplicating this literal "本功能仅支持群组使用" 3 times. | ✅ 已修复并验证：提取 `GROUP_ONLY_MESSAGE` 并替换三处；字面量计数测试与编译通过。 |
| 108 | Issue | 次要（MINOR） | `tools.py` | 49 | `python:S7503` | Use asynchronous features in this function or remove the `async` keyword. | ✅ 已修复并验证：依赖注入函数改为同步函数；仓库内不存在 await 调用，AST 签名测试与编译通过。 |
| 109 | Issue | 主要（MAJOR） | `tools.py` | 131 | `python:S1066` | Merge this if statement with the enclosing one. | ✅ 已修复并验证：QQBot 头像回退抽取并合并绑定 QQ 判断，不再存在原嵌套 if；校准复杂度降至 2，编译通过。 |
| 110 | Issue | 严重（CRITICAL） | `tools.py` | 244 | `python:S1192` | Define a constant instead of duplicating this literal 'base64://' 4 times. | ✅ 已修复并验证：提取 `BASE64_PREFIX` 并复用解析与消息构建；原字面量仅保留定义一处，Base64 行为测试通过。 |
| 111 | Issue | 次要（MINOR） | `tools.py` | 407 | `python:S1481` | Remove the unused local variable "name". | ✅ 已修复并验证：节点长图不再读取未显示的名称；AST 不存在该局部赋值，编译通过。 |
| 112 | Issue | 次要（MINOR） | `tools.py` | 412 | `python:S1481` | Remove the unused local variable "name_height". | ✅ 已修复并验证：删除未使用的名称高度；AST 不存在该局部赋值，编译通过。 |
| 113 | Issue | 主要（MAJOR） | `tools.py` | 421 | `python:S125` | Remove this commented out code. | ✅ 已修复并验证：删除废弃的名称绘制注释代码；源码回归测试与编译通过。 |

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

