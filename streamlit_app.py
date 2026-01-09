print("--- Partner's Shift Pay Calculator ---")

# 1. Collect the pay rate
base_rate = float(input("Enter normal hourly rate: $"))

# 2. Collect the hours for each category
normal_hrs = float(input("Enter normal (daytime) hours worked: "))
night_hrs = float(input("Enter night shift hours (6pm-8am): "))
weekend_hrs = float(input("Enter weekend hours: "))

# 3. Calculate the Pay for each "bucket"
# Normal pay
pay_normal = normal_hrs * base_rate

# Night pay (adds 15% loading)
pay_night = night_hrs * (base_rate * 1.15)

# Weekend pay (1.5x or 150%)
pay_weekend = weekend_hrs * (base_rate * 1.5)

# 4. Final Totals
total_hours = normal_hrs + night_hrs + weekend_hrs
total_pay = pay_normal + pay_night + pay_weekend

print("\n" + "="*30)
print(f"Total Hours Worked: {total_hours}")
print(f"Normal Pay:   ${pay_normal:.2f}")
print(f"Night Pay:    ${pay_night:.2f} (15% loading included)")
print(f"Weekend Pay:  ${pay_weekend:.2f} (1.5x rate included)")
print("-" * 30)
print(f"GROSS TOTAL:  ${total_pay:.2f}")
print("="*30)

input("\nPress Enter to exit.")
