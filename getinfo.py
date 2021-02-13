from bilibili_api import bangumi, video

class Information:
    
    def __init__(self, title):
        self.title = title
        self.cid_list = []
        self.title_list = []
        self.save_info = {}
        self.n = 0
    def add_episode(self, cid, title):
        self.n = self.n + 1
        self.cid_list.append(cid)
        self.title_list.append(title)

def get_bv(bvid):
    info = video.get_video_info(bvid=bvid)
    result = Information(info['title'])
    pages = info['pages']
    for page in pages:
        result.add_episode(page['cid'], page['part'])
    save_info = {
        'type': 'video',
        'aid': info['aid'],
        'bvid': info['bvid'],
        'title': info['title'],
        'cover': info['pic'],
        'username': info['owner']['name'],
        'user-avatar': info['owner']['face'],
        'pages': []
    }
    for page in pages:
        save_info['pages'].append({
            'cid': page['cid'],
            'title': page['part']
        })
    result.save_info = save_info
    return result

def get_av(aid):
    info = video.get_video_info(aid=aid)
    result = Information(info['title'])
    pages = info['pages']
    for page in pages:
        result.add_episode(page['cid'], page['part'])
    save_info = {
        'type': 'video',
        'aid': info['aid'],
        'bvid': info['bvid'],
        'title': info['title'],
        'cover': info['pic'],
        'username': info['owner']['name'],
        'user-avatar': info['owner']['face'],
        'pages': []
    }
    for page in pages:
        save_info['pages'].append({
            'cid': page['cid'],
            'title': page['part']
        })
    result.save_info = save_info
    return result

def get_md(media_id):
    media_id = int(media_id)
    meta = bangumi.get_meta(media_id=media_id)
    season_id = meta['media']['season_id']
    collective_info = bangumi.get_collective_info(season_id=season_id)
    result = Information(meta['media']['title'])
    for episode in collective_info['episodes']:
        result.add_episode(episode['cid'], episode['long_title'])
    save_info = {
        'type': 'bangumi',
        'media_id': media_id,
        'season_id': season_id,
        'title': meta['media']['title'],
        'cover': meta['media']['cover'],
        'content_type': meta['media']['type_name'],
        'episodes': []
    }
    for episode in collective_info['episodes']:
        episode_info = {
            'aid': episode['aid'],
            'bvid': episode['bvid'],
            'cid': episode['cid'],
            'epid': episode['id'],
            'cover': episode['cover'],
            'title': episode['long_title']
        }
        save_info['episodes'].append(episode_info)
    result.save_info = save_info
    return result

def get(video_type, video_id):
    if video_type == 'BV':
        return get_bv(video_id)
    elif video_type == 'av':
        return get_av(video_id)
    else: # md
        return get_md(video_id)