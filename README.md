# Youtube Annotations Downloader Plugin

This plugin adds the ability to download annotations from Youtube. 

Annotations from Youtube have been removed from the platform since 2019. However, they are still present in archives like https://storage.googleapis.com/biggest_bucket/annotations, so they are still reachable.

This plugin downloads those archived annotations and adds them as subtitles under the languagecode `annotations`.

## Installation 
Check the [how to install yt-dlp plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) section to learn how to install this and other plugins.

## Usage
This plugin adds the annotations as the "languagecode" `annotations`. This means that, for downloading them, you have to use `--sub-langs annotations`. 

## Observations
* As the plugin basically adds a new subtitle "language", the infojson will have a new "annotations" key in the "subtitles" dictionary.
* As the annotations are treated as subtitles, their filename is the same as the other subtitles. In other words, the `subtitle` template for the [output template](https://github.com/yt-dlp/yt-dlp#output-template) will dictate their filename.
* The annotation file is a not embeddable .xml. This means that forcing it to be embedded into containers that support xml files (.mkv) with `--embed-subs` will result in a ffmpeg error, although if more embeddable languages are downloaded yt-dlp will manage to embed those. Other sub related parameters which call a ffmpeg conversion like `--convert-subs` will also trigger ffmpeg errors, but if more convertible subs are downloaded, yt-dlp will manage to convert those to the desired format. If you want to download annotations, it is adviced to explicitly use conversions from one format to another (for example, use `--convert-subs vtt>srt` instead of `--convert-subs srt`) to avoid getting those errors.