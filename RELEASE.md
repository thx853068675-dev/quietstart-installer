# 轻启 0.9.52

本次提供三种下载：

| 场景 | 下载 |
| --- | --- |
| 首次安装，Mac Apple 芯片 | `quietstart-0.9.52-macOS-arm64-bundle.zip` |
| 首次安装，Windows x64 | `quietstart-0.9.52-Windows-x64-bundle.zip` |
| 已有小白轻启整合版，只升级应用 | `quietstart-0.9.52.hap` |

两个整合 ZIP 均包含修改后的小白调试助手、同一份轻启 HAP 和使用说明。无需额外安装 DevEco Studio、SDK、Java、Python 或重签脚本。独立 HAP 与整合包内 HAP 的 SHA-256 相同。

## 安装与升级

1. 首次使用请完整解压整合 ZIP；已有支持“内外重签＋手动选版”的小白轻启整合版，可只下载独立 HAP。
2. 手机开启开发者模式、USB 调试，连接电脑并允许调试。在助手中登录自己的华为账号。
3. 点“选择 HAP”或“更换版本”，选中新版 HAP，确认显示 **0.9.52**，再点“开始调试”。助手会申请设备授权，将内部工作模块与主包一起重新签名后安装。
4. 手机打开轻启，按向导开启无线调试，填写当前端口并完成本机连接。轻启自行更新工作模块，显示“在线”后即可拔线使用。

**独立 HAP 仍需通过整合助手重签，不是所有手机通用的直装包。** 普通小白官方版没有本整合版新增的内外重签流程。签名不一致时请先检查材料；不要为了升级直接卸载而丢失规则。

## 轻启更新

- 新增用户点击引导学习；规则区分手动与自动来源，可配置自动启用，并支持单条删除。
- 优化多种开屏按钮识别、实际点击位置和 S01～S08 策略展示，统一规则卡片、圆环与位置示意。
- 修复工作模块同版本重复更新的安装状态处理；概览按实际点击累计跳过数。
- 本机连接配置独立监督：区分心跳、工作进展和 RPC，最多自动恢复 3 次；用户结束时同步停止。
- 增加本地系统退出记录；恢复时减少重复打开首页，正常后台检测不会主动打开轻启。

## 验证与范围

轻启 582 项 Node 回归和 6 项监督脚本场景测试通过，0.9.52 主包与内嵌模块构建、版本和完整性检查通过。Pura X / HarmonyOS 7 已完成模块自安装、真实广告点击、拔线故障恢复、有限重试和主动停止测试；后续会话存续约 5 小时，6 次休眠等待后恢复健康，自动恢复次数为 0。原定两小时逐分钟采样提前停止，未宣称完整连续采样通过。

Mac、Windows 整合版由相同固定上游源码构建；实际构建和签名测试结果见关联 Actions。此前 Mac 整合版完成过真机内外重签与本机激活验证。Windows 真机安装、其他华为账号、HarmonyOS 6.1、24 小时运行和真实耗电仍未完整验证。异常恢复可能短暂出现系统启动画面；AGC 工作模块安装链路仍不在此次支持范围内。

Mac 修改版未做 Apple 公证，确认来源后可按“隐私与安全性”提示打开。支持 Apple 芯片 Mac 和 Windows x64；不包含 Intel Mac、Windows ARM。

## 来源

这是轻启维护者修改版，不是小白官方发布版。小白源码基线为 `likuai2010/auto-installer` 的 `24388dd86e6c3c7cab83fc27d3e6f4f9cb1b7801`；发布者已确认取得修改与再分发授权，第三方部分不自动适用轻启 MIT 许可。

[开始使用](https://github.com/thx853068675-dev/quietstart-installer/blob/main/USAGE.md) · [轻启配图说明](https://github.com/thx853068675-dev/quietstart/blob/main/docs/USAGE.md) · [后台验证记录](https://github.com/thx853068675-dev/quietstart/blob/main/docs/LIFECYCLE.md) · [小白官方源码与下载](https://github.com/likuai2010/auto-installer/releases/latest) · [第三方说明](https://github.com/thx853068675-dev/quietstart-installer/blob/main/THIRD-PARTY.md)
