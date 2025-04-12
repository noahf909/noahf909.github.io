# Load the original file and clean it up
with open("nemoursml_time_based_gantt.txt", "r", encoding="utf-8") as file:
    raw_lines = file.readlines()

# Prepare cleaned lines with proper milestone formatting
cleaned_lines = []
milestone_count = 1

for line in raw_lines:
    line_strip = line.strip()
    if line_strip.lower().startswith("milestone"):
        # Add milestone keyword and unique ID
        cleaned_lines.append(
            f"{line_strip} : milestone, m{milestone_count}, {line_strip.split(':')[-1].strip()}, 1m\n"
        )
        milestone_count += 1
    elif "Milestone" in line_strip and "milestone" not in line_strip:
        # Fix incorrect milestone line
        parts = line_strip.split(":")
        if len(parts) >= 2:
            task_name = parts[0].strip()
            start_time = parts[1].split(",")[0].strip()
            cleaned_lines.append(
                f"{task_name} : milestone, m{milestone_count}, {start_time}, 1m\n"
            )
            milestone_count += 1
    else:
        cleaned_lines.append(line)

# Save cleaned chart to new file
output_cleaned_path = "nemoursml_time_based_gantt_cleaned.txt"
with open(output_cleaned_path, "w", encoding="utf-8") as file:
    file.writelines(cleaned_lines)

output_cleaned_path
