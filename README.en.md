[![Deutsch](https://img.shields.io/badge/🇩🇪%20-German-blue)](README.md)

---

![Last update](https://img.shields.io/github/last-commit/moehrem/hass-webio?label=last%20update)  
[![GitHub Release](https://img.shields.io/github/v/release/moehrem/hass-webio?sort=semver)](https://github.com/moehrem/hass-webio/releases)  
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/moehrem/hass-webio)  
![GitHub last commit](https://img.shields.io/github/last-commit/moehrem/hass-webio)  
![GitHub issues](https://img.shields.io/github/issues/moehrem/hass-webio)  

![HA Analytics](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Fcustom_integrations.json&query=%24.hass-webio.total&label=Active%20Installations)  
[![HACS](https://img.shields.io/badge/HACS-Integration-blue.svg)](https://github.com/hacs/integration)  
[![HASS QS](https://github.com/moehrem/hass-webio/actions/workflows/hass.yml/badge.svg)](https://github.com/moehrem/hass-webio/actions/workflows/hass.yml)  
[![HACS QS](https://github.com/moehrem/hass-webio/actions/workflows/hacs.yml/badge.svg)](https://github.com/moehrem/hass-webio/actions/workflows/hacs.yml)

---

<div align="center" style="display: flex; align-items: center; justify-content: center; gap: 1rem; flex-wrap: wrap;">

<a href="https://www.wut.de">
  <img src="https://www.wut.de/pics/icon/e-wwwww-wt-grww-000.svg" alt="Wiesemann & Theis GmbH" height="80">
</a>

<h1 style="margin: 0;">W&amp;T webIO for Home Assistant</h1>

</div>

---

This integration enables connecting **Wiesemann & Theis** webIO devices to Home Assistant.

> **Disclaimer:**  
> This project is not affiliated with Wiesemann & Theis GmbH and is not officially supported by them.

> **Note:**  
> The integration is still under development. Features may be missing and bugs may occur. Feel free to test it and [open an issue](https://github.com/moehrem/hass-webio/issues) if you find problems or have feature requests!

---

## 📦 Compatibility

Based on the Programming Manual **1.73** (as of 11/2024). Compatible devices include:

- Web-IO Digital 4.0  
- Web-IO Analog 4.0  
- Web Thermometer  
- Web Thermo-Hygrometer  
- Web Thermo-Hygrobarometer  

---

## 🔧 Features

- **REST API**: Fetches and sets data as JSON  
- **Outputs**: Exposed as switches (usable manually or in automations)  
- **Inputs & Counters**: Read-only sensors  

---

## 📂 Installation

### 🏆 HACS (recommended)

1. [install HACS](https://www.hacs.xyz/docs/use/)
2. [![add custom repo to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=moehrem&repository=hass-webio&category=Integration)
3. **Setup**: Click "Download" at the bottom right.

### 🔧 Manual Installation

1. [Download the latest release](https://github.com/moehrem/hass-webio/releases/latest)  
2. Extract the files into `config/custom_components/hass-webio/`

---

## ⚙️ Configuration

1. Enter the **IP address** of your webIO device  
2. (Optional) Provide a **password** if your device is secured  
3. Name your **inputs**  
4. Name your **outputs**  

Once completed, Home Assistant will discover the sensors and switches of your W&T webIO device.```
