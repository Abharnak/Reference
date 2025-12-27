To do:
- organize measures ->create table, folders 1_,2_,..
<img width="10" height="40" alt="image" src="https://github.com/user-attachments/assets/665eec51-4b96-4025-8d59-0b48e0d10835" />

- create table to show totcolumn front for solution,inc
- total column front & bold no CG
- Same column Width use measure, auto column width
- Tooltip
- name measures meaningfully
- document measures and their relation between each other
- 

# Tips
- alt+ctrl+shift+L => delects all same value
# 1. How to bring total column in first position in matrix visual

Reference: "https://www.youtube.com/watch?v=VRUs0pWgsdE"

1. Create new table in power query with columns that will be used in matrix view
<img width="449" height="580" alt="image" src="https://github.com/user-attachments/assets/781809b5-ea19-4303-ba70-8c6b01da5510" />

2. Connect column in use to fact table column in modelling view
   
4. Use Column(column in use) from created table in matrix view eg
<img width="238" height="249" alt="image" src="https://github.com/user-attachments/assets/320fb351-b338-4dab-af90-5ea3047311e4" />

5. In Data Pane, Click on Column(column in use) and sort by Column click order.
   
7. If need to change font color or back ground use separate measure for modifying that use that measure in cell elements field in visualization pane

## Measure for total column background color:
```
TotalColumn = 
SWITCH(
    SELECTEDVALUE('Category-Sales-Table'[Category in use]),
    "Total","#252423",BLANK())
```

8. Filter customer name by sales value by right clicking on 3 dots select sort choose sales measure created and then ascending or descending.
   <img width="884" height="348" alt="image" src="https://github.com/user-attachments/assets/697487ed-7450-4737-b6c8-cee67d42b75f" />

# 2. How to add custom column Tooltip in Matrix
