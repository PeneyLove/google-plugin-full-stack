// 选择所有视频元素
const videoElements = document.querySelectorAll('video');

// 为每个视频元素添加选择功能
videoElements.forEach((video) => {
    const container = video.closest('.video-container'); // 假设视频容器有这个类名
    if (container) {
        container.style.border = '2px solid transparent';
        container.addEventListener('click', () => {
            if (container.style.borderColor === 'red') {
                container.style.borderColor = 'transparent';
            } else {
                container.style.borderColor = 'red';
            }
            // 向插件主程序发送选择状态
            chrome.runtime.sendMessage({
                type: 'videoSelection',
                videoId: video.id,
                isSelected: container.style.borderColor === 'red'
            });
        });
    }
});