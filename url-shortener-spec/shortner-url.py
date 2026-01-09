import api
import storage
import sys

def print_menu():
    print("\n=== URL Shortener (is.gd) ===")
    print("1. ✂️  Shorten URL")
    print("2. 📂 List Links")
    print("3. 🔍 Search")
    print("4. 📊 Statistics")
    print("5. 🗑️  Delete Link")
    print("0. 🚪 Exit")
    print("=============================")

def handle_add():
    url = input("Enter URL to shorten: ").strip()
    if not url:
        return
    
    alias = input("Enter custom alias (optional, min 5 chars, leave empty for random): ").strip()
    category = input("Enter category (optional): ").strip()
    
    # Handle empty strings as None
    alias = alias if alias else None
    
    if alias:
        if len(alias) > 12:
            print("❌ Error: Custom alias cannot exceed 12 characters.")
            return
        if len(alias) < 5:
             print("⚠️  Warning: Custom alias usually needs 5+ chars for is.gd.")

    category = category if category else None
    
    print(f"✂️  Shortening {url}...")
    try:
        short_url, error = api.shorten_url(url, alias)
        
        if error:
            print(f"❌ API Error: {error}")
            return

        print(f"DEBUG: API returned short_url={short_url}")
        
        # Requests: "non salvare il link" -> Disable storage
        # link = storage.add_link(url, short_url, alias, category)
        
        print(f"✅ Success! Short URL: {short_url}")
        print(f"   Original: {url}")
        if alias:
            print(f"   Alias: {alias}")
    except Exception as e:
        import traceback
        print("\n❌ CRITICAL ERROR CAUGHT:")
        traceback.print_exc()

def handle_list():
    links = storage.get_links()
    if not links:
        print("📭 No links found.")
        return
    
    print(f"\n📂 Found {len(links)} links:")
    for l in links:
        alias_info = f" (Alias: {l['alias']})" if l['alias'] else ""
        cat_info = f" [Cat: {l['category']}]" if l['category'] else ""
        print(f" - {l['short_url']} -> {l['original_url']}{alias_info}{cat_info}")

def handle_search():
    query = input("Enter search query (alias or URL): ").strip()
    if not query:
        return

    results = storage.find_link(query)
    if not results:
        print(f"🔍 No results for '{query}'")
        return
        
    print(f"\n🔍 Found {len(results)} matches for '{query}':")
    for l in results:
        alias_info = f" (Alias: {l['alias']})" if l['alias'] else ""
        print(f" - {l['short_url']} -> {l['original_url']}{alias_info}")

def handle_stats():
    links = storage.get_links()
    if not links:
        print("📭 No data available.")
        return

    print("\n📊 Statistics")
    print(f"Total Links: {len(links)}")
    
    categories = set(l['category'] for l in links if l['category'])
    print(f"Categories: {len(categories)} ({', '.join(categories)})")
    
    print("\n🆕 Most Recent Links:")
    recent = links[-3:]
    recent.reverse()
    for l in recent:
        print(f" - {l['short_url']} ({l['created_at']})")

def handle_delete():
    identifier = input("Enter ID or Alias to delete: ").strip()
    if not identifier:
        return

    if storage.delete_link(identifier):
        print(f"🗑️  Deleted link '{identifier}'")
    else:
        print(f"⚠️  Link '{identifier}' not found")

def main():
    while True:
        print_menu()
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            handle_add()
        elif choice == '2':
            handle_list()
        elif choice == '3':
            handle_search()
        elif choice == '4':
            handle_stats()
        elif choice == '5':
            handle_delete()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    # Checking for simple connectivity to ensure "venv" or environment isn't blocking basic networking
    # Since we use standard library urllib, this should work everywhere Python 3 is installed.
    main()
