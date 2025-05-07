import js from '@eslint/js';
import react from 'eslint-plugin-react';

export default [
  js.configs.recommended,
  {
    files: ['**/*.jsx', '**/*.js'],
    plugins: {
      react: react,
    },
    languageOptions: {
      parserOptions: {
        ecmaFeatures: {
          jsx: true,
        },
        ecmaVersion: 'latest',
        sourceType: 'module',
      },
    },
    settings: {
      react: {
        version: 'detect',
      },
    },
    rules: {
      "no-undef": 'warn',
      "no-unused-vars": "warn",
      'react/react-in-jsx-scope': 'warn',
      'react/jsx-uses-react': 'warn',
    },
  },
];