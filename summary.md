---
title: "technicalSummary"
author: "Ozgur"
date: '2023-03-07'
output: 
  html_document:
    keep_md: true
---



Importing libraries

```r
library(tidyverse)
```

```
## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.0 ──
```

```
## ✓ ggplot2 3.3.3     ✓ purrr   0.3.4
## ✓ tibble  3.1.6     ✓ dplyr   1.0.7
## ✓ tidyr   1.1.4     ✓ stringr 1.4.0
## ✓ readr   2.1.2     ✓ forcats 0.5.1
```

```
## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
## x dplyr::filter() masks stats::filter()
## x dplyr::lag()    masks stats::lag()
```

```r
library(grDevices)
library(DT)
```

## Explanation for Investing Download Part

## Importing Data 


```r
df <- read_csv("data.csv")
```

```
## New names:
## * Daily -> Daily...31
## * Daily -> Daily...34
```

```
## Rows: 23 Columns: 39
## ── Column specification ────────────────────────────────────────────────────────
## Delimiter: ","
## chr  (29): Name, Symbol, Exchange, Bid, Ask, Extended Hours, Extended Hours ...
## dbl   (1): Chg.
## time  (1): Time
## 
## ℹ Use `spec()` to retrieve the full column specification for this data.
## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
```

## Calculate Pivot and Resistance/Supports
This calculation is based on https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/pivot-points-resistance-support


```r
df <- df %>% mutate(Pivot = round((Last+High+Low)/3,2)) %>%
  mutate(Res1 = round(2*Pivot - Low, 2),
         Sup1 = round(2*Pivot - High, 2),
         Res2 = round(Pivot + Res1 - Sup1, 2),
         Sup2 = round(Pivot - Res1 + Sup1, 2),
         Res3 = round(High + 2*(Pivot - Low), 2),
         Sup3 = round(Low - 2*(High - Pivot), 2))
```

## Colorful Technical Summary

You could check the color names here. Distinct argument could be FALSE to see variations.

```r
grDevices::colors(distinct = TRUE)
```

Set colors for each signal. 

```r
signals <- c("Strong Buy", "Buy", "Neutral", "Sell", "Strong Sell")
signalColors <- c("darkgreen", "palegreen", "lavender", "tomato", "firebrick")
```

Select our columns and format their background colors 

```r
dftmp <- df %>% select(Symbol, `5 Minutes`:Monthly, Sup3, Sup2, Sup1, Pivot, Res1, Res2, Res3, Last, `Chg. %`)
colnames(dftmp)[1:9] <- c("Symbol", "5Min","15Min", "30Min","Hourly","5Hours","Daily","Weekly","Monthly")
datatable(dftmp) %>% formatStyle(names(dftmp), backgroundColor = styleEqual(signals, signalColors)) %>%
  formatStyle(columns = c("Res1","Res2","Res3"), target = "cell", color = "red") %>% 
  formatStyle(columns = c("Sup1","Sup2","Sup3"), target = "cell", color = "green")
```

```{=html}
<div id="htmlwidget-fa7a17f5473ccd874297" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-fa7a17f5473ccd874297">{"x":{"filter":"none","vertical":false,"data":[["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"],["BIOEN.IS","ESEN.IS","YEOTK.IS","GSDHO.IS","NATEN.IS","MAVI.IS",".XGIDA","TUPRS.IS","TCELL.IS","SISE.IS","KOZAL.IS",".XMANA","AKSEN.IS","GARAN.IS","AKBNK.IS","EREGL.IS","FROTO.IS","SAHOL.IS","KCHOL.IS","TOASO.IS","THYAO.IS",".XU100","HEKTS.IS"],["Strong Buy","Neutral","Strong Buy","Strong Buy","Neutral","Strong Buy","Strong Buy","Strong Buy","Strong Sell","Neutral","Strong Sell","Strong Sell","Strong Sell","Neutral","Strong Sell","Strong Sell","Strong Sell","Strong Sell","Strong Sell","Strong Sell","Sell","Strong Sell","Strong Sell"],["Strong Buy","Strong Sell","Strong Buy","Strong Buy","Neutral","Strong Buy","Strong Buy","Strong Buy","Strong Sell","Neutral","Strong Sell","Strong Sell","Strong Buy","Sell","Strong Sell","Sell","Strong Sell","Strong Sell","Strong Sell","Strong Sell","Sell","Strong Sell","Strong Sell"],["Strong Buy","Sell","Strong Buy","Strong Buy","Neutral","Neutral","Strong Buy","Strong Buy","Strong Sell","Neutral","Strong Sell","Strong Sell","Strong Sell","Neutral","Neutral","Strong Sell","Neutral","Sell","Neutral","Strong Sell","Strong Sell","Sell","Strong Sell"],["Strong Buy","Neutral","Strong Buy","Strong Buy","Neutral","Buy","Strong Buy","Strong Buy","Sell","Buy","Strong Sell","Strong Sell","Strong Sell","Strong Buy","Buy","Buy","Buy","Neutral","Strong Buy","Sell","Sell","Neutral","Strong Sell"],["Strong Buy","Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Neutral","Strong Buy","Strong Sell","Neutral","Sell","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Buy","Strong Buy","Strong Sell"],["Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Sell","Strong Buy","Strong Sell","Strong Buy","Strong Sell","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Sell"],["Strong Buy","Neutral","Strong Buy","Buy","Neutral","Neutral","Strong Buy","Strong Buy","Neutral","Strong Buy","Sell","Strong Buy","Neutral","Neutral","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Neutral"],["Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Strong Buy","Buy"],[16.25,62.84,61.35,3.08,128.6,102.1,4686.92,610.94,30.1,46.78,18.76,12866.56,33.28,23.94,17.33,42.88,588.74,42.26,79.74,178.16,135.8,5219.78,32.3],[16.5,64.67,64.55,3.13,140.4,103.9,4717.25,618.37,31.15,47.8,19.47,13155.91,33.69,24.78,17.96,43.6,601.17,43.57,81.87,183.03,138.4,5298.57,33.14],[16.86,65.84,67.85,3.22,146.3,105.5,4771.8,632.14,31.68,48.31,19.86,13300.59,33.94,25.22,18.29,43.96,609.14,44.22,82.94,185.96,139.7,5340.23,33.56],[17.11,67.67,71.05,3.27,158.1,107.3,4802.13,639.57,32.73,49.33,20.57,13589.94,34.35,26.06,18.92,44.68,621.57,45.53,85.07,190.83,142.3,5419.02,34.4],[17.47,68.84,74.35,3.36,164,108.9,4856.68,653.34,33.26,49.84,20.96,13734.62,34.6,26.5,19.25,45.04,629.54,46.18,86.14,193.76,143.6,5460.68,34.82],[17.72,70.67,77.55,3.41,175.8,110.7,4887.01,660.77,34.31,50.86,21.67,14023.97,35.01,27.34,19.88,45.76,641.97,47.49,88.27,198.63,146.2,5539.47,35.66],[18.08,71.84,80.85,3.5,181.7,112.3,4941.56,674.54,34.84,51.37,22.06,14168.65,35.26,27.78,20.21,46.12,649.94,48.14,89.34,201.56,147.5,5581.13,36.08],[17.22,67,71.15,3.32,152.2,107.1,4826.35,645.9,32.2,48.82,20.24,13445.26,34.2,25.66,18.62,44.32,617.1,44.88,84,188.9,141,5381.9,33.98],["+2.20%","-2.19%","+3.19%","+4.40%","-9.89%","+0.19%","+2.49%","+3.78%","-1.23%","-2.65%","-1.46%","-1.31%","+0.29%","-0.16%","-0.69%","-0.18%","+0.05%","-2.14%","-0.59%","-2.23%","-0.98%","-0.19%","-2.07%"]],"container":"<table class=\"display\">\n  <thead>\n    <tr>\n      <th> <\/th>\n      <th>Symbol<\/th>\n      <th>5Min<\/th>\n      <th>15Min<\/th>\n      <th>30Min<\/th>\n      <th>Hourly<\/th>\n      <th>5Hours<\/th>\n      <th>Daily<\/th>\n      <th>Weekly<\/th>\n      <th>Monthly<\/th>\n      <th>Sup3<\/th>\n      <th>Sup2<\/th>\n      <th>Sup1<\/th>\n      <th>Pivot<\/th>\n      <th>Res1<\/th>\n      <th>Res2<\/th>\n      <th>Res3<\/th>\n      <th>Last<\/th>\n      <th>Chg. %<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"columnDefs":[{"className":"dt-right","targets":[10,11,12,13,14,15,16,17]},{"orderable":false,"targets":0}],"order":[],"autoWidth":false,"orderClasses":false,"rowCallback":"function(row, data, displayNum, displayIndex, dataIndex) {\nvar value=data[1]; $(this.api().cell(row, 1).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[2]; $(this.api().cell(row, 2).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[3]; $(this.api().cell(row, 3).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[4]; $(this.api().cell(row, 4).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[5]; $(this.api().cell(row, 5).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[6]; $(this.api().cell(row, 6).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[7]; $(this.api().cell(row, 7).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[8]; $(this.api().cell(row, 8).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[9]; $(this.api().cell(row, 9).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[10]; $(this.api().cell(row, 10).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[11]; $(this.api().cell(row, 11).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[12]; $(this.api().cell(row, 12).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[13]; $(this.api().cell(row, 13).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[14]; $(this.api().cell(row, 14).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[15]; $(this.api().cell(row, 15).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[16]; $(this.api().cell(row, 16).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[17]; $(this.api().cell(row, 17).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[18]; $(this.api().cell(row, 18).node()).css({'background-color':value == \"Strong Buy\" ? \"darkgreen\" : value == \"Buy\" ? \"palegreen\" : value == \"Neutral\" ? \"lavender\" : value == \"Sell\" ? \"tomato\" : value == \"Strong Sell\" ? \"firebrick\" : null});\nvar value=data[14]; $(this.api().cell(row, 14).node()).css({'color':'red'});\nvar value=data[15]; $(this.api().cell(row, 15).node()).css({'color':'red'});\nvar value=data[16]; $(this.api().cell(row, 16).node()).css({'color':'red'});\nvar value=data[12]; $(this.api().cell(row, 12).node()).css({'color':'green'});\nvar value=data[11]; $(this.api().cell(row, 11).node()).css({'color':'green'});\nvar value=data[10]; $(this.api().cell(row, 10).node()).css({'color':'green'});\n}"}},"evals":["options.rowCallback"],"jsHooks":[]}</script>
```
