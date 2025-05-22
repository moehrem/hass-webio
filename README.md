[![English](https://img.shields.io/badge/🇬🇧%20-English-blue)](README.en.md)

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

<h1 style="margin: 0;">W&amp;T webIO für HomeAssistant</h1>

</div>

---

Diese Integration unterstützt die Anbindung von webIO-Geräten von **Wiesemann & Theis** an HomeAssistant.

> **Disclaimer:**  
> Die Entwicklung steht in keiner Verbindung mit Wiesemann & Theis GmbH und wird vom Unternehmen nicht unterstützt.

> **Hinweis:**  
> Die Integration befindet sich in Entwicklung. Funktionen können fehlen und Fehler auftreten. Testen auf eigene Gefahr und bitte bei Bugs oder Feature-Wünschen ein [Issue eröffnen](https://github.com/moehrem/hass-webio/issues).

---

## 📦 Kompatibilität

Basierend auf dem Programmierhandbuch **1.73** (Stand 11/2024). Unterstützte Geräte:

- Web-IO Digital 4.0
- Web-IO Analog 4.0
- Web-Thermometer
- Web-Thermo-Hygrometer
- Web-Thermo-Hygrobarometer

---

## 🔧 Funktionsumfang

- **REST-API**: Liest und setzt Daten als JSON
- **Outputs**: Werden als Schalter abgebildet (manuell oder in Automationen)
- **Inputs & Counter**: Als Sensoren verfügbar (nicht steuerbar)

---

## 📂 Installation

### 🏆 HACS (empfohlen)

1. HACS installieren:  
   https://www.hacs.xyz/docs/use/
2. Repository hinzufügen:  
   https://my.home-assistant.io/redirect/hacs_repository/?owner=moehrem&repository=hass-webio&category=Integration  
3. In HACS unten rechts auf **Herunterladen** klicken.

### 🔧 Manuelle Installation

1. [Letzten Release herunterladen](https://github.com/moehrem/hass-webio/releases/latest)  
2. Dateien nach `config/custom_components/hass-webio/` entpacken

---

## ⚙️ Einrichtung

1. **IP-Adresse** des Geräts eingeben  
2. (Optional) **Passwort** hinterlegen  
3. **Inputs** benennen  
4. **Outputs** benennen  

Fertig! HomeAssistant entdeckt nun die Sensoren und Schalter Ihres W&T webIO.```