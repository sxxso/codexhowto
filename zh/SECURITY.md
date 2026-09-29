# 安全策略

## 适用范围

codexhowto 是一个文档与模板仓库,不提供任何运行时服务。主要的安全考量是:

- **模板安全** —— 示例 `config.toml`、脚本和提示词都应示范安全的默认设置。
- **不含密钥** —— 任何文件中都不得包含真实的 API key、token 或凭据。

## 报告漏洞

如果你发现某个模板可能把用户引向不安全的配置(例如脚本在容器之外默认使用 `--dangerously-bypass-approvals-and-sandbox`,或某个示例会泄露密钥),请私下报告,而不要公开提交 issue。

1. 使用仓库的私密漏洞报告功能,或
2. 直接联系维护者。

**请勿**为安全问题公开提交 issue。

## 安全模板准则

贡献任何示例时,请遵守以下规则:

- 默认采用在仍能完成任务的前提下**最严格**的审批策略与沙箱模式(日常工作用 `on-request` + `workspace-write`;审查用 `read-only`)。
- 只在明确标注的容器/CI 场景中展示 `--dangerously-bypass-approvals-and-sandbox`,并始终配上 **Warning** 提示。
- 绝不硬编码凭据。使用环境变量(`OPENAI_API_KEY`)和占位符。
- 未解释风险前,不要在 `[sandbox_workspace_write]` 中启用 `network_access`。

完整的安全模型见[审批与沙箱](05-approvals-sandbox/)。
