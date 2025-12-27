## 1. How to bring total column in first position in matrix visual

1. Create new table in power query
<img width="449" height="580" alt="image" src="https://github.com/user-attachments/assets/781809b5-ea19-4303-ba70-8c6b01da5510" />
2. connect column in use to fact table column
3. use column from created column in use in matrix view eg
<img width="238" height="249" alt="image" src="https://github.com/user-attachments/assets/320fb351-b338-4dab-af90-5ea3047311e4" />
4. right click on column in use and sort by order
5. if need to change font color or back ground use separate measure for modifying that use that measure in cell elements field

## Measure for total column background color:
```
TotalColumn = 
SWITCH(
    SELECTEDVALUE('Category-Sales-Table'[Category in use]),
    "Total","#252423",BLANK())
```

