# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

A sari-sari store needs to keep track of several products. Each product may have information such as:
- product name
- price
- quantity or available stock


## MUST EXPLAIN
- how the concept can be used in the sari-sari store inventory system

- what data, object, property or method may be involved

- how applying the concept can improve the organization or design of the program.

### 1. Encapsulation
To keep the products organized, encapsulation can be used to make sure that all the products are labeled correctly. Before anything can even be done, all products must have their correct values. Say, a bottle of shampoo can't be labeled as cup noodles, and a piece of candy can't have the price of a bag of chips. So, grouping the product, its name, its price, and any other important thing together can be done with encapsulation. This concept can improve organization by avoiding any errors like incorrect price tags or quantity available, which may impact the store negatively.

### 2. Abstraction
A way asbtraction can be applied to help with keeping track of the store's inventory is by having a system where in the salesperson has a task of inputting which products have been sold so the quantity can always be updated. They do not need to know what the process behind it is, they just need to keep track. This helps the store by keeping its stock updated while also not giving the salesperson a hard time by trying to get them to understand any complex things that may come with the program.

### 3. Inheritance
Many products may have different variations like flavors to them. Inheritance can be used by having the parent classes be the "main" category of the product and the child classes as the variations or flavors of it, since not all the time the products have the same prices to them. For example, skyflakes has its regular plain crackers, but it also has the ones with sweet filling in them. Most of the time, the ones with filling are more expensive than the regular ones, so even if it is technically the same brand and the product is almost the same, we can not label it as the same object. With this, the parent class can be like the regular skyflakes and the children are the different flavors like the ones with condensada in it, so that the different values can be changed while they are still grouped together. This can help by eliminating the repititive input of a new object even if it is almost the same as a different one.

### 4. Polymorphism
Not all products are packed the same way. A carton of milk does not have the same amount as a carton of eggs. A pack of noodles may have 5 packets in it, but a pack of crackers may have around 10 packets. Depending on how each store tracks the quantity of their goods, they may need specific ways of tracking per product, which is where polymorphism can help. Polymorphism can allow for the use of the same function of unpacking for all but it adds a different amount to the quantity depending on the product. This saves the creation of multiple functions for the same purpose of unpacking and updating stock.

## Reflection
Out of the four pillars of OOP, I believe that polymorphism would be the most useful one in improving the store's inventory system. This is because it allows for flexibility across all the stores objects. It can not only help with the restocking process of different products, because it can also help with the amount of change given depending on the amount a customer gave which helps with money, or maybe even with quality checking different products to see if any of the perishable goods have already gone bad. In short, it can be used for almost anything, so that is why I believe it is the most useful out of the four.