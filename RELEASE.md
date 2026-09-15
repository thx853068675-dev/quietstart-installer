重点适配 **HarmonyOS 6.1（API 24）**，保留 HarmonyOS 7 支持。

- 优化广告识别、点击速度和强化学习，改善卓易通应用名称及启动处理。
- 加强后台异常恢复与退出诊断；连续失败按 5 / 15 / 30 / 60 秒重试，达到上限后停止。
- 优化本机连接进度，连接成功后自动开启跳过。

6.1 真机完成 30 分钟压力测试：9 次系统低内存回收均自动恢复。恢复期间仍可能短暂中断，并非永不被杀。

**下载：**首次安装选 Mac Apple 芯片或 Windows x64 整合 ZIP（含小白修改版、HAP 和说明）；已有轻启整合助手只需下载 `quietstart-0.9.55.hap`。

**使用：**解压整合包 → 连接手机、登录华为账号 → 选择 HAP → 开始调试 → 手机按向导完成本机连接。HAP 仍需为自己的手机重签，内置工作模块会一并处理，无需 DevEco 或 SDK。

[详细步骤](https://github.com/thx853068675-dev/quietstart-installer/blob/main/USAGE.md) · [测试报告](https://github.com/thx853068675-dev/quietstart/blob/main/docs/pressure-test-6.1-0.9.60.md) · [第三方说明](https://github.com/thx853068675-dev/quietstart-installer/blob/main/THIRD-PARTY.md)
