mtcars
mean(mtcars$cyl)
mean(mtcars$mpg)
median(mtcars$cyl)
var(mtcars$cyl)
cov(mtcars$mpg,mtcars$cyl)
sd(mtcars$cyl)
hist(mtcars$cyl)
#hist(mpg)
hist(mtcars$cyl,
     xlab="Miles per Calls(Cyl)",
     main="Histogram in MTCARS",
     breaks=12,
     col="dodgerblue",
     border="black")
hist(mtcars$cyl,
     xlab="Miles per Calls(Cyl)",
     ylab="Length",
     main="Histogram in MTCARS",
     breaks=20,
     col="yellow",
     border="red")
barplot(table(mtcars$cyl))
barplot(table(mtcars$mpg))
boxplot(mtcars$cyl)
unique(mtcars$cyl)
boxplot(mtcars)
boxplot(cars$speed)
unique(cars$speed)
  