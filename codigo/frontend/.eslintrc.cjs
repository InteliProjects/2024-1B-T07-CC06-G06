module.exports = {
  root: true, // Set root to true
  env: { browser: true, es2020: true }, // Set environment to browser and ES2020
  extends: [ // Extend eslint configurations
    'eslint:recommended', // Use eslint recommended rules
    'plugin:react/recommended', // Use recommended react rules
    'plugin:react/jsx-runtime', // Use JSX runtime plugin
    'plugin:react-hooks/recommended', // Use recommended react hooks rules
  ],
  ignorePatterns: ['dist', '.eslintrc.cjs'], // Ignore specific patterns
  parserOptions: { ecmaVersion: 'latest', sourceType: 'module' }, // Set parser options
  settings: { react: { version: '18.2' } }, // Set react version
  plugins: ['react-refresh'], // Enable react-refresh plugin
  rules: { // Define rules
    'react/jsx-no-target-blank': 'off', // Disable rule for no target blank
    'react-refresh/only-export-components': [ // Define rule for react-refresh plugin
      'warn', // Set warning level
      { allowConstantExport: true }, // Allow constant export
    ],
  },
}
