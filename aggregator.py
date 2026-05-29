def aggregate_results(text_results,audio_results,video_result):
    text_score=text_results.get('score',0.0)
    audio_score=audio_results.get('score',0.0)
    video_score=video_result.get('score',0.0)
    max_score=max(text_score,audio_score,video_score)
    if max_score>=0.60:
        final_verdict='UNSAFE'
    else:
        final_verdict='SAFE'
    results=[]
    if text_score>=0.60:
        results.append(f'text metadata flagged: {text_results.get("reason")}')
    elif audio_score>=0.60:
        results.append(f'Audio Voice flagged: {audio_results.get("reason")}')
    elif video_score>=0.60:
        results.append(f'video content flagged:{video_result.get("reason")}')
    
    if not results:
        results.append('All channels passed the safety test')
    final_report = {
        "verdict": final_verdict,
        "overall_risk_score": max_score,
        "flags_triggered": results,
        "breakdown": {
            "text_channel_score": text_score,
            "audio_channel_score": audio_score,
            "video_channel_score": video_score
        }
    }
    return final_report