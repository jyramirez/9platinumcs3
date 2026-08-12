# Computational Thinking Exercise
## [Smart Vending Machine]

**Name:** Jenelle Ysabel C. Ramirez
**Section:** 9 - Platinum
**Last Name:** Ramirez
**Date:** 08/12/26

--

## Step 1: Identify the Big Problem
### Main Problem

In this scenario, the main problem is that the vending machine does not work properly and efficiently.

--

## Step 2: Identify the Sub-Problems

1. There are times where the vending machine does not give the correct change.

2. The machine does not track the status of the items, and whether or not there is still stock.

3. The vending machine has no/incorrect labels for the items and buttons, which leads to the student getting the wrong thing.

4. The machine lacks efficiency when multiple students use it in a row.

--

## Step 3: Apply Computational Thinking Skills

| Sub-Problem | CT Skill | Proposed Solution |

|---|---|---|

| Sub-problem 1: Incorrect Change | Algorithm Design | I will first check if there are any internal issues such as blockages, and after which depending on what I find, I will fix the issue and then refill the vending machine with the change. |

| Sub-problem 2: Lack of Item Tracking | Decomposition | I will create new systems that will help with inventory. The first one could count what Items are present, the second one could track if the vending machine is restocked or people are buying, and the third could use the second system to notify the people if the items have run out. |

| Sub-problem 3: Incorrect Items | Abstraction | I will focus purely on assigning the right buttons to the right items, and I may also add extra labels in case the students need it. |

| Sub-problem 4: Efficiency | Pattern Recognition | I will observe why the vending machine is not efficient when many people do not use it in a row, and I will base my solution on that. |

--

## Step 4: Algorithmic Solution

### Selected Sub-Problem

Sub-problem 1: Incorrect Change

### Pseudocode
START

Open vending machine

Check internal parts

IF blockage is present THEN
    Clear up blockage
    Refill change

ELSE
    Check other internal parts
    Fix issue
    Refill change

END
---