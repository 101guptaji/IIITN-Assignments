#binomial dist
rm(list=ls())
n=10
p=.22
x=3
print(dbinom(x,n,p))
p1=1-pbinom(3,n,p)
print(p1)

#poison dist
lambda=1.5
x=0
print(dpois(x,lambda))

##Negative Binomial Distribution
x=4
r=2
p=.05
p2=1-pnbinom(x,r,p)
print(p2)