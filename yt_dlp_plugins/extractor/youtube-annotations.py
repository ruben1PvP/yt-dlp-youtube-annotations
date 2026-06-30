from yt_dlp.extractor.youtube import YoutubeIE

class _YoutubeAnnotationsIE(YoutubeIE, plugin_name='youtube-annotations'):
    def _real_extract(self, url):
        info = super()._real_extract(url)
 
        # Alternative: video_id = info['id']
        video_id = str(self.extract_id(url))
        
        annotation_url = 'https://storage.googleapis.com/biggest_bucket/annotations/'+video_id[0]+'/'+video_id[0:3]+'/'+video_id+'.xml.gz'
        
        info['subtitles'].setdefault('annotations', []).append({'url': annotation_url, 'ext': 'xml'})

        return info
