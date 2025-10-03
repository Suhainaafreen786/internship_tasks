import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

df = pd.read_csv("sales.csv")
summary = df.groupby("Product")["Sales"].sum()
avg_sales = df["Sales"].mean()

plt.figure(figsize=(8,5))
summary.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.close()

doc = SimpleDocTemplate("Sales_Report.pdf")
styles = getSampleStyleSheet()
content = []

content.append(Paragraph("<b>Automated Sales Report</b>", styles["Title"]))
content.append(Spacer(1,12))
content.append(Paragraph(f"Average Sales: {avg_sales:.2f}", styles["Normal"]))
content.append(Spacer(1,12))
content.append(Paragraph("Sales Summary:", styles["Heading2"]))

for product, value in summary.items():
    content.append(Paragraph(f"{product}: {value}", styles["Normal"]))

content.append(Spacer(1,12))
content.append(Image("sales_chart.png", width=400, height=300))
doc.build(content)

print("✅ Report Generated: Sales_Report.pdf")