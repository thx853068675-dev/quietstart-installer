# 小白调试助手 · 轻启整合

**[下载 Mac / Windows 整合包](https://github.com/thx853068675-dev/quietstart-installer/releases)** · [轻启应用源码](https://github.com/thx853068675-dev/quietstart)

面向用户的步骤见 [开始使用](USAGE.md)。整合 ZIP 附带 HAP；助手不预选版本，用户手动选择 HAP 后读取包内实际版本，无需开发环境或脚本。

## 源码和构建

此目录保存轻启原创的 Dart 签名模块、源码改造脚本和打包脚本。构建时读取固定修订的小白源码，不在本仓库复制其整套代码或预编译签名材料。第三方权利见 [说明](THIRD-PARTY.md)。

1. 获取 `likuai2010/auto-installer` 的 `24388dd86e6c3c7cab83fc27d3e6f4f9cb1b7801` 修订。
2. 准备轻启 0.9.52 原始发布 HAP，SHA-256：`cc099cd3f066962e0f6504a4f46867bfecdbe9bbe9c7f743dcfa72d3d23acb05`。
3. 执行 `python prepare.py --source <小白源码目录> --hap <原始HAP>`。此命令只针对干净的固定源码执行一次，不能重复覆盖已经修改过的工作区。
4. 在 `flutter/hap_installer` 中执行 `flutter pub get`，再执行 `flutter build macos --release` 或 `flutter build windows --release`。
5. 执行 `python package.py --source <小白源码目录> --hap <原始HAP> --platform macOS-arm64`；Windows 使用 `Windows-x64`。

构建使用 Flutter 3.29.3。Mac 构建机需要 Xcode/CocoaPods，Windows 构建机需要 Visual Studio C++ 工具链。**这些是维护者的编译依赖，不是用户重签时的依赖。** GitHub Actions 的 `XiaoBai integrated bundles` 工作流执行以上过程。

## 签名路径

`CmdService.signHap` 检测轻启包名，进入 `QuietStartAdapter.dart`：

1. 固定本次输入、证书、Profile 和 PEM 私钥的副本。
2. 校验内部模块及其清单，移除旧 ZIP 签名封装，调用小白原生 `signer` 重签工作模块。
3. 核对程序内容与 Profile，更新内置模块的长度和 SHA-256。
4. 重签主包，检查内外版本、内容、Profile，然后交给原安装流程。

输入的原始 HAP 保持不变；每次独立临时目录在成功或失败后清理。损坏的轻启包不会退回“只签外包”的旧路径。其他应用继续使用小白原流程。

## 验证范围

- `core` 中执行 `dart pub get && dart test` 测试失败拦截与内外签名编排。
- 设置 `QUIETSTART_TEST_HAP` 为真实 0.9.52 HAP 路径，会额外检查华为 ZIP 对齐填充及内嵌模块。
- 本地用集成后的 Dart 签名路径生成过实际内外重签包，并用官方工具独立验证了两层签名。官方工具只用于开发验证，集成版不调用它。
- `signedProfile` 是签名块结构与 Profile 一致性检查，不能替代密码学验签；手机安装服务执行最终验签。原生签名器的 `verify-app` 会对非法输入返回成功，因此集成层不使用该结果。
- 自动编译、签名测试和真机安装验证应分别记录，不将构建通过表述为端到端安装通过。

## 迁移来源

从 [quietstart 的 `60ee16b` 修订](https://github.com/thx853068675-dev/quietstart/tree/60ee16b11cb56da3e14de1efd0a5f38e67f6d318/integrations/xiaobai)独立迁移。应用代码留在原仓库；整合工具的维护、问题反馈和下载在本仓库。原始开发历史可通过该链接追溯。
