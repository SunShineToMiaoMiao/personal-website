// https://eslint.org/docs/user-guide/configuring

module.exports = {
    root: true,
    parserOptions: {
        parser: 'babel-eslint'
    },
    env: {
        browser: true,
    },
    extends: [
        // https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
        // consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
        'plugin:vue/essential',
        // https://github.com/standard/standard/blob/master/docs/RULES-en.md
        'standard'
    ],
    // check if imports actually resolve
    settings: {
        'import/resolver': {
            webpack: {
                config: 'build/webpack.base.conf.js',
            },
        },
    },
    // required to lint *.vue files
    plugins: [
        'vue'
    ],
    // add your custom rules here
    rules: {
        // allow async-await
        'generator-star-spacing': 'off',
        // allow debugger during development
        'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
        //去掉有闭合标签的检查
        'vue/no-parsing-error': [2, {"x-invalid-end-tag": false}],
        //启用console
        'no-console': 'off',
        //函数名后的空格
        'space-before-function-paren':["error", "never"],
        // 空格4个
        // 'indent': ['error', 4, {'SwitchCase': 1}],
        'indent': 'off',
      "no-trailing-spaces": "error",
        //开启分号
        "semi": "error",
        "no-multiple-empty-lines": [1, {"max": 2}],//空行最多不能超过2行
        'vue/script-indent': [
            'error',
            2,
            {
                'baseIndent': 1
            }
        ]
    }
}
