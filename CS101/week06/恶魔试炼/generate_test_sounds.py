"""
生成测试音效文件
使用pygame生成简单的WAV音效
"""

import pygame
import numpy as np
import os

# 初始化pygame mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

def generate_tone(frequency, duration, volume=0.5, fade_out=True):
    """生成单一音调"""
    sample_rate = 44100
    num_samples = int(sample_rate * duration)
    
    # 生成正弦波
    t = np.linspace(0, duration, num_samples, False)
    wave = np.sin(2 * np.pi * frequency * t)
    
    # 添加淡入淡出
    if fade_out:
        fade_length = int(sample_rate * 0.05)  # 50ms淡出
        fade_envelope = np.ones(num_samples)
        fade_envelope[-fade_length:] = np.linspace(1, 0, fade_length)
        wave *= fade_envelope
    
    # 调整音量
    wave *= volume
    
    # 转换为16位整数
    wave = (wave * 32767).astype(np.int16)
    
    # 立体声
    stereo_wave = np.column_stack((wave, wave))
    
    return stereo_wave

def generate_jump_sound():
    """生成跳跃音效（上升音调）"""
    sample_rate = 44100
    duration = 0.25
    num_samples = int(sample_rate * duration)
    
    t = np.linspace(0, duration, num_samples, False)
    # 频率从低到高
    frequency = 300 + 600 * (t / duration)
    wave = np.sin(2 * np.pi * frequency * t)
    
    # 淡出
    fade_length = int(sample_rate * 0.05)
    fade_envelope = np.ones(num_samples)
    fade_envelope[-fade_length:] = np.linspace(1, 0, fade_length)
    wave *= fade_envelope
    
    wave *= 0.5
    wave = (wave * 32767).astype(np.int16)
    stereo_wave = np.column_stack((wave, wave))
    
    return stereo_wave

def generate_land_sound():
    """生成落地音效（短促撞击）"""
    sample_rate = 44100
    duration = 0.15
    num_samples = int(sample_rate * duration)
    
    t = np.linspace(0, duration, num_samples, False)
    # 低频撞击声
    wave = np.sin(2 * np.pi * 150 * t)
    wave += np.sin(2 * np.pi * 100 * t) * 0.5
    
    # 快速衰减
    envelope = np.exp(-t * 30)
    wave *= envelope
    
    wave *= 0.6
    wave = (wave * 32767).astype(np.int16)
    stereo_wave = np.column_stack((wave, wave))
    
    return stereo_wave

def generate_fail_sound():
    """生成失败音效（下降音调）"""
    sample_rate = 44100
    duration = 1.0
    num_samples = int(sample_rate * duration)
    
    t = np.linspace(0, duration, num_samples, False)
    # 频率从高到低
    frequency = 600 - 400 * (t / duration)
    wave = np.sin(2 * np.pi * frequency * t)
    
    # 淡出
    fade_length = int(sample_rate * 0.1)
    fade_envelope = np.ones(num_samples)
    fade_envelope[-fade_length:] = np.linspace(1, 0, fade_length)
    wave *= fade_envelope
    
    wave *= 0.5
    wave = (wave * 32767).astype(np.int16)
    stereo_wave = np.column_stack((wave, wave))
    
    return stereo_wave

def generate_win_sound():
    """生成胜利音效（欢快上升）"""
    sample_rate = 44100
    duration = 1.5
    
    # 多个音调组合
    notes = [523, 659, 784, 1047]  # C大调和弦
    segments = []
    
    for i, freq in enumerate(notes):
        seg_duration = 0.3
        num_samples = int(sample_rate * seg_duration)
        t = np.linspace(0, seg_duration, num_samples, False)
        wave = np.sin(2 * np.pi * freq * t)
        
        # 淡入淡出
        fade_length = int(sample_rate * 0.05)
        fade_envelope = np.ones(num_samples)
        fade_envelope[:fade_length] = np.linspace(0, 1, fade_length)
        fade_envelope[-fade_length:] = np.linspace(1, 0, fade_length)
        wave *= fade_envelope
        
        wave *= 0.4
        wave = (wave * 32767).astype(np.int16)
        segments.append(wave)
    
    # 组合
    total_length = sum(len(s) for s in segments)
    final_wave = np.zeros((total_length, 2), dtype=np.int16)
    
    pos = 0
    for seg in segments:
        stereo_seg = np.column_stack((seg, seg))
        final_wave[pos:pos+len(seg)] = stereo_seg
        pos += len(seg)
    
    return final_wave

def generate_menu_sound():
    """生成菜单音效（短促点击）"""
    sample_rate = 44100
    duration = 0.08
    num_samples = int(sample_rate * duration)
    
    t = np.linspace(0, duration, num_samples, False)
    wave = np.sin(2 * np.pi * 800 * t)
    
    # 快速衰减
    envelope = np.exp(-t * 50)
    wave *= envelope
    
    wave *= 0.3
    wave = (wave * 32767).astype(np.int16)
    stereo_wave = np.column_stack((wave, wave))
    
    return stereo_wave

def generate_hurt_sound():
    """生成受伤音效"""
    sample_rate = 44100
    duration = 0.3
    num_samples = int(sample_rate * duration)
    
    t = np.linspace(0, duration, num_samples, False)
    # 不和谐音
    wave = np.sin(2 * np.pi * 200 * t)
    wave += np.sin(2 * np.pi * 250 * t) * 0.3
    
    # 衰减
    envelope = np.exp(-t * 10)
    wave *= envelope
    
    wave *= 0.5
    wave = (wave * 32767).astype(np.int16)
    stereo_wave = np.column_stack((wave, wave))
    
    return stereo_wave

def generate_bgm():
    """生成8位风格循环BGM（地狱癫狂风格 - 无缝循环+强节奏）"""
    sample_rate = 44100
    duration = 8.0  # 缩短到8秒，更容易无缝循环
    num_samples = int(sample_rate * duration)
    
    t = np.linspace(0, duration, num_samples, False)
    
    # 主旋律 - 使用大调，更明亮
    melody_notes = [
        523.25,  # C5
        587.33,  # D5
        659.25,  # E5
        783.99,  # G5
        880.00,  # A5
        698.46,  # F5 (半音，增加癫狂)
        622.25,  # Eb5 (半音，增加癫狂)
    ]
    
    melody = np.zeros(num_samples)
    
    # 节奏模式 - 强节奏感（0.2秒每拍）
    beat_duration = 0.2  # 每拍0.2秒（150 BPM）
    
    # 旋律模式 - 确保头尾衔接（40拍 = 8秒）
    melody_pattern = [0, 2, 4, 5, 6, 4, 2, 0,
                      1, 3, 5, 6, 4, 2, 0, 1,
                      0, 2, 4, 5, 6, 4, 2, 0,
                      1, 3, 5, 6, 4, 2, 0, 0,
                      0, 2, 4, 5, 6, 4, 2, 0]
    
    for note in range(len(melody_pattern)):
        note_start = int(note * beat_duration * sample_rate)
        note_length = int(beat_duration * sample_rate * 0.7)  # 70%时长
        
        if note_start + note_length <= num_samples:
            freq = melody_notes[melody_pattern[note]]
            
            # 三角波
            wave = 2 * np.abs(2 * (freq * np.arange(note_length) / sample_rate % 1) - 1) - 1
            
            # 包络 - 快速起音，快速衰减（强节奏感）
            envelope = np.ones(note_length)
            attack = int(note_length * 0.05)
            decay = int(note_length * 0.4)
            envelope[:attack] = np.linspace(0, 1, attack)
            envelope[attack:attack+decay] = np.linspace(1, 0.2, decay)
            
            wave *= envelope * 0.2
            melody[note_start:note_start + note_length] += wave
    
    # 贝斯线 - Walking Bass（确保循环，40拍）
    bass_pattern = [130.81, 146.83, 164.81, 196.00] * 9 + [130.81, 146.83, 164.81, 130.81, 130.81, 130.81, 130.81, 130.81]
    bass = np.zeros(num_samples)
    
    for beat in range(len(bass_pattern)):
        beat_start = int(beat * beat_duration * sample_rate)
        beat_length = int(beat_duration * sample_rate)
        
        if beat_start + beat_length <= num_samples:
            freq = bass_pattern[beat]
            bass_wave = np.sign(np.sin(2 * np.pi * freq * t[beat_start:beat_start + beat_length]))
            
            envelope = np.ones(beat_length)
            fade = int(beat_length * 0.15)
            envelope[:fade] = np.linspace(0, 1, fade)
            envelope[-fade:] = np.linspace(1, 0.6, fade)
            
            bass_wave *= envelope * 0.2
            bass[beat_start:beat_start + beat_length] += bass_wave
    
    # 鼓点 - 强节奏
    drums = np.zeros(num_samples)
    for beat in range(int(duration / beat_duration)):
        beat_start = int(beat * beat_duration * sample_rate)
        
        if beat % 4 == 0:  # 强拍
            drum_length = int(0.2 * sample_rate)
            if beat_start + drum_length <= num_samples:
                drum_t = np.linspace(0, 0.2, drum_length, False)
                drum = np.sin(2 * np.pi * 80 * drum_t) * np.exp(-drum_t * 15)
                drums[beat_start:beat_start + drum_length] += drum * 0.4
        elif beat % 2 == 0:  # 弱拍
            drum_length = int(0.1 * sample_rate)
            if beat_start + drum_length <= num_samples:
                drum_t = np.linspace(0, 0.1, drum_length, False)
                drum = np.sin(2 * np.pi * 120 * drum_t) * np.exp(-drum_t * 25)
                drums[beat_start:beat_start + drum_length] += drum * 0.25
        else:  # 半拍
            drum_length = int(0.05 * sample_rate)
            if beat_start + drum_length <= num_samples:
                drum_t = np.linspace(0, 0.05, drum_length, False)
                drum = np.random.randn(drum_length) * np.exp(-drum_t * 40)
                drums[beat_start:beat_start + drum_length] += drum * 0.1
    
    # 混合
    final_wave = melody + bass + drums
    
    # 限制振幅
    max_val = np.max(np.abs(final_wave))
    if max_val > 0:
        final_wave = final_wave / max_val * 0.65
    
    # 无缝循环 - 头尾淡入淡出
    fade_samples = int(0.01 * sample_rate)
    if fade_samples < len(final_wave):
        fade_in = np.linspace(0, 1, fade_samples)
        fade_out = np.linspace(1, 0, fade_samples)
        final_wave[:fade_samples] *= fade_in
        final_wave[-fade_samples:] *= fade_out
    
    final_wave = (final_wave * 32767).astype(np.int16)
    stereo_wave = np.column_stack((final_wave, final_wave))
    
    return stereo_wave

def save_wav(filename, wave_data):
    """保存为WAV文件"""
    pygame.mixer.quit()
    pygame.init()
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
    
    sound = pygame.sndarray.make_sound(wave_data)
    
    # 使用scipy保存（如果可用）
    try:
        from scipy.io import wavfile
        wavfile.write(filename, 44100, wave_data)
        print(f"✓ 生成 {filename}")
    except ImportError:
        # 备用方法
        import wave
        import struct
        
        with wave.open(filename, 'w') as wav_file:
            wav_file.setnchannels(2)
            wav_file.setsampwidth(2)
            wav_file.setframerate(44100)
            
            for sample in wave_data:
                wav_file.writeframes(struct.pack('<hh', sample[0], sample[1]))
        
        print(f"✓ 生成 {filename} (备用方法)")

# 创建sounds目录
os.makedirs("sounds", exist_ok=True)

print("开始生成测试音效...")
print("="*50)

# 生成所有音效
save_wav("sounds/jump.wav", generate_jump_sound())
save_wav("sounds/land.wav", generate_land_sound())
save_wav("sounds/fail.wav", generate_fail_sound())
save_wav("sounds/win.wav", generate_win_sound())
save_wav("sounds/menu.wav", generate_menu_sound())
save_wav("sounds/hurt.wav", generate_hurt_sound())
save_wav("sounds/bgm.wav", generate_bgm())  # 新增BGM

print("="*50)
print("所有音效生成完成！")
print("文件位置: sounds/ 文件夹")
print("\n现在可以运行: pgzrun test_sound.py")
