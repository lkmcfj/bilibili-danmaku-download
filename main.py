import sys
import os
import argparse
import json
import bilibili_api
import getinfo, common

def check_arguments(args):
    if args.id is None:
        print('specify target video through --id ID')
        return False
    if args.type is None:
        print('specify video id type through --type TYPE')
        return False
    if (args.type != 'BV') and (args.type != 'av') and (args.type != 'md'):
        print('invalid argument TYPE')
        return False
    if not os.path.isdir(args.output):
        print('invalid output path')
        return False
    return True

def main():
    parser = argparse.ArgumentParser(description='download bilibili danmaku')
    parser.add_argument(
        '--id', metavar='ID',
        help='use a BV number, av number or bangumi media id to specify target video')
    parser.add_argument(
        '-t', '--type', metavar='TYPE',
        help='TYPE=BV/av/md'
    )
    parser.add_argument(
        '-o', '--output', metavar='OUTPUT_PATH', default='.',
        help='files will be saved in OUTPUT_PATH, or a new subdirectory in OUTPUT_PATH, depending on --mkdir argument. OUTPUT_PATH is default to working path'
    )
    parser.add_argument(
        '--mkdir', action='store_true', default=False,
        help='make new subdirectory in OUTPUT_PATH'
    )
    parser.add_argument(
        '--use-name', action='store_true', default=False,
        help='use video title as the name of subdirectory, video parts and episodes'
    )
    parser.add_argument(
        '--save-info', action='store_true', default=False,
        help='create a json file containing video information'
    )

    args = parser.parse_args()
    if not check_arguments(args):
        sys.exit()
    
    print('Collecting information')
    info = getinfo.get(args.type, args.id)
    print('Title:', info.title)
    print('Video number:', info.n)
    if args.use_name:
        subdir = common.escape_filename(info.title)
    else:
        subdir = args.type + args.id
    if args.mkdir:
        target_path = os.path.join(args.output, subdir)
        if not os.path.isdir(target_path):
            os.mkdir(target_path)
    else:
        target_path = args.output

    if args.use_name:
        xml_list = [os.path.join(target_path, common.escape_filename(f'{i+1}.{title}.xml')) for i, title in enumerate(info.title_list)]
    else:
        xml_list = [os.path.join(target_path, str(_ + 1) + '.xml') for _ in range(info.n)]
    url_list = [common.comments_url(cid) for cid in info.cid_list]
    print('Downloading')
    common.download(url_list, xml_list)
    if args.use_name:
        info_json_filename = common.escape_filename(info.title + '.json')
    else:
        info_json_filename = args.type + args.id + '.json'
    with open(os.path.join(target_path, info_json_filename), 'w', encoding='utf-8') as info_f:
        json.dump(info.save_info, info_f, ensure_ascii=False, indent=4)
    print('Complete.')
