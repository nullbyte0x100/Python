# To illustrate simple right circular cone
cone <- function(x, y){
  sqrt(x ^ 2 + y ^ 2)
}

# prepare variables.
x <- y <- seq(-1, 1, length = 30)
z <- outer(x, y, cone)

# plot the 3D surface
persp(x, y, z)
