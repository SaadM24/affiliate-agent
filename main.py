import os
from datetime import datetime
from agent.processor import process_emails

def save_report(results):
    """Saves the full briefing report to the output folder"""

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"output/briefing_{timestamp}.txt"

    with open(filename, 'w') as f:
        f.write("REVWISE AFFILIATE PARTNER DAILY BRIEFING\n")
        f.write(f"Generated: {datetime.now().strftime('%d %B %Y, %H:%M')}\n")
        f.write("=" * 60 + "\n\n")

        for result in results:
            f.write(f"{result['email']}\n")
            f.write("-" * 40 + "\n")
            f.write("ANALYSIS:\n")
            f.write(result['analysis'] + "\n\n")
            f.write("RECOMMENDED ACTION:\n")
            f.write(result['action'] + "\n")
            f.write("\n" + "=" * 60 + "\n\n")

    return filename

def main():
    print("RevWise Affiliate Intelligence Agent")
    print("=" * 40)
    print("Reading partner emails...\n")

    emails_path = "data/emails.txt"

    if not os.path.exists(emails_path):
        print(f"Error: Could not find {emails_path}")
        return

    results = process_emails(emails_path)

    report_file = save_report(results)

    print(f"\n{'='*50}")
    print(f"Done! Processed {len(results)} emails.")
    print(f"Report saved to: {report_file}")
    print("\nPREVIEW OF FIRST RESULT:")
    print("=" * 50)

    if results:
        print(f"\n{results[0]['email']}")
        print(results[0]['analysis'])
        print(results[0]['action'])

if __name__ == "__main__":
    main()