library(data.table)
library(ggplot2)

dt <- data.table(
  gene = c("BRCA1", "TP53", "EGFR"),
  expression = c(12.3, 45.6, 7.8)
)
print(dt)

p <- ggplot(dt, aes(x = gene, y = expression)) + geom_col()
ggsave("expression_demo.png", p)
cat("Plot saved to expression_demo.png\n")
