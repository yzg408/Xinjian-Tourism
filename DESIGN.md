---
version: alpha
name: 新建大观
description: 新国潮·全域智慧文旅平台 — 一眼越千年，一城揽新建
colors:
  primary: "#C9A84C"
  primary-light: "#E8D5A3"
  primary-dark: "#A8883A"
  secondary: "#2E86AB"
  secondary-light: "#6BB8D4"
  secondary-dark: "#1B5E7A"
  accent: "#E8734A"
  accent-light: "#F5A78A"
  accent-dark: "#C95C38"
  canvas: "#FDF8F0"
  canvas-alt: "#F5F0E8"
  ink: "#2C2416"
  body: "#6B5E4A"
  muted: "#9A8E7A"
  white: "#FFFFFF"
  hairline: "#E8E0D0"
  scrim: "rgba(44, 36, 22, 0.6)"
typography:
  hero-display:
    fontFamily: "'Noto Serif SC', 'Source Han Serif SC', serif"
    fontSize: clamp(2.5rem, 6vw, 4rem)
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: "0.05em"
  display-lg:
    fontFamily: "'Noto Serif SC', 'Source Han Serif SC', serif"
    fontSize: clamp(2rem, 4vw, 2.8rem)
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.03em"
  display-md:
    fontFamily: "'Noto Serif SC', 'Source Han Serif SC', serif"
    fontSize: clamp(1.5rem, 3vw, 2rem)
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "0.02em"
  display-sm:
    fontFamily: "'Noto Serif SC', 'Source Han Serif SC', serif"
    fontSize: clamp(1.2rem, 2vw, 1.5rem)
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "0.02em"
  headline:
    fontFamily: "'Noto Serif SC', 'Source Han Serif SC', serif"
    fontSize: clamp(1.1rem, 1.8vw, 1.3rem)
    fontWeight: 600
    lineHeight: 1.3
  body-lg:
    fontFamily: "-apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 1.0625rem
    fontWeight: 400
    lineHeight: 1.7
  body:
    fontFamily: "-apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.7
  body-sm:
    fontFamily: "-apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
  caption:
    fontFamily: "-apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 0.75rem
    fontWeight: 400
    lineHeight: 1.4
  button:
    fontFamily: "-apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 1rem
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "0.02em"
  nav-link:
    fontFamily: "-apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 0.9375rem
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.02em"
spacing:
  xxs: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  xxl: 64px
  section: 80px
rounded:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  full: 9999px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
    rounded: "{rounded.md}"
    padding: 12px 28px
    fontFamily: "{typography.button.fontFamily}"
    fontSize: "{typography.button.fontSize}"
    fontWeight: "{typography.button.fontWeight}"
    border: "none"
    boxShadow: "0 4px 14px rgba(201, 168, 76, 0.35)"
  button-primary-hover:
    backgroundColor: "{colors.primary-dark}"
    boxShadow: "0 6px 20px rgba(201, 168, 76, 0.5)"
    transform: "translateY(-2px)"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 12px 28px
    border: "2px solid {colors.primary}"
    fontWeight: 600
  button-outline-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.white}"
  card-scenic:
    backgroundColor: "{colors.white}"
    rounded: "{rounded.lg}"
    padding: "{spacing.md}"
    boxShadow: "0 4px 20px rgba(44, 36, 22, 0.08)"
  card-scenic-hover:
    boxShadow: "0 8px 30px rgba(44, 36, 22, 0.15)"
    transform: "translateY(-4px)"
  hero-overlay:
    background: "linear-gradient(135deg, rgba(44,36,22,0.7) 0%, rgba(46,134,171,0.4) 100%)"
  section-title:
    fontFamily: "{typography.display-md.fontFamily}"
    fontSize: "{typography.display-md.fontSize}"
    fontWeight: "{typography.display-md.fontWeight}"
    color: "{colors.primary-dark}"
    textAlign: "center"
    borderBottom: "3px solid"
    borderImage: "linear-gradient(90deg, {colors.primary}, {colors.accent}) 1"
---
