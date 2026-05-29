from pathlib import Path

import pipelines
import preprocessor
import aggregator


def content_moderation(video_path,user_text=""):
    
    print("STARTING AI CONTENT MODERATION")
    print("\n stage 1: preprocessing the data")
    audio_file=preprocessor.extract_audio(video_path)
    video_file=preprocessor.extract_frames(video_path)

    print("\n stage 2: Running AI safety scanners")
    text_report=pipelines.analyze_text(user_text)
    audio_report=pipelines.analyze_audio(audio_file)
    video_report=pipelines.analyze_video(video_file)

    print('\n Blending scores for the ultimate decision')
    final_report = aggregator.aggregate_results(
        text_results=text_report,
        audio_results=audio_report,
        video_result=video_report)
    print(f"\nFINAL VERDICT:{final_report['verdict']}")

    return final_report
if __name__ == "__main__":
    test_video = "uploads/sample_video.mp4"
    test_text = "Watch this exclusive tutorial where I show you how to hack into my router!"

    if Path(test_video).exists():
        report_output = content_moderation(test_video, test_text)
        print("\nStructure of Final Output Package:")
        import pprint
        pprint.pprint(report_output)
    else:
        print(f"\n[Notice] To test main.py directly from your terminal, place a video file at: {test_video}")