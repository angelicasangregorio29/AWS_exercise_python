import argparse
import api
import storage
import sys

def cmd_add(args):
    print(f"✂️  Shortening {args.url}...")
    short_url, error = api.shorten_url(args.url, args.alias)
    if error:
        print(f"❌ Error: {error}")
        return

    link = storage.add_link(args.url, short_url, args.alias, args.category)
    print(f"✅ Success! Short URL: {short_url}")
    print(f"   Original: {args.url}")
    if link['alias']:
        print(f"   Alias: {link['alias']}")
    if link['category']:
        print(f"   Category: {link['category']}")

def cmd_list(args):
    links = storage.get_links()
    if not links:
        print("📭 No links found.")
        return
    
    print(f"📂 Found {len(links)} links:")
    for l in links:
        alias_info = f" (Alias: {l['alias']})" if l['alias'] else ""
        cat_info = f" [Cat: {l['category']}]" if l['category'] else ""
        print(f" - {l['short_url']} -> {l['original_url']}{alias_info}{cat_info}")

def cmd_search(args):
    results = storage.find_link(args.query)
    if not results:
        print(f"🔍 No results for '{args.query}'")
        return
        
    print(f"🔍 Found {len(results)} matches for '{args.query}':")
    for l in results:
        alias_info = f" (Alias: {l['alias']})" if l['alias'] else ""
        print(f" - {l['short_url']} -> {l['original_url']}{alias_info}")

def cmd_delete(args):
    if storage.delete_link(args.identifier):
        print(f"🗑️  Deleted link with identifier '{args.identifier}'")
    else:
        print(f"⚠️  Link not found: '{args.identifier}'")

def cmd_stats(args):
    links = storage.get_links()
    if not links:
        print("📭 No data available.")
        return

    print("📊 Statistics")
    print(f"Total Links: {len(links)}")
    
    categories = set(l['category'] for l in links if l['category'])
    print(f"Categories: {len(categories)} ({', '.join(categories)})")
    
    # Most recent
    print("\n🆕 Most Recent Links:")
    # Assuming list is appended, so last is newest. Or sort by created_at.
    # storage.add_link appends, so last is newest.
    recent = links[-3:] # Last 3
    recent.reverse()
    for l in recent:
        print(f" - {l['short_url']} ({l['created_at']})")

def main():
    parser = argparse.ArgumentParser(description="URL Shortener CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # ADD
    parser_add = subparsers.add_parser('add', help='Shorten a new URL')
    parser_add.add_argument('url', help='The URL to shorten')
    parser_add.add_argument('--alias', help='Optional custom alias')
    parser_add.add_argument('--category', help='Optional category')
    parser_add.set_defaults(func=cmd_add)

    # LIST
    parser_list = subparsers.add_parser('list', help='List all links')
    # Make subparser not require arguments for list
    parser_list.set_defaults(func=cmd_list)

    # SEARCH
    parser_search = subparsers.add_parser('search', help='Search links')
    parser_search.add_argument('query', help='Search query (alias or URL)')
    parser_search.set_defaults(func=cmd_search)

    # DELETE
    parser_delete = subparsers.add_parser('delete', help='Delete a link')
    parser_delete.add_argument('identifier', help='ID or Alias of the link to delete')
    parser_delete.set_defaults(func=cmd_delete)

    # STATS
    parser_stats = subparsers.add_parser('stats', help='Show statistics')
    parser_stats.set_defaults(func=cmd_stats)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
